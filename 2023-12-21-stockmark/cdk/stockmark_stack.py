from aws_cdk import (
    Stack,
    aws_iam as iam,
    aws_ec2 as ec2,
    CfnOutput
)
from constructs import Construct


class StockmarkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        stack_name = "stockmark-stack-dev"

        # ロールの作成とIAMポリシー
        web_server_role = iam.Role(
            self,
            f"{stack_name}-ec2-role",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "AmazonSSMManagedInstanceCore"
                )
            ],
        )
        # VPCを作成
        vpc = ec2.Vpc(
            self,
            f"{stack_name}-vpc",
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    cidr_mask=24,
                    name="public",
                    subnet_type=ec2.SubnetType.PUBLIC
                )
            ]
        )

        # EC2インスタンスのセキュリティグループを作成する
        security_group = ec2.SecurityGroup(
            self,
            f"{stack_name}-sg",
            vpc=vpc,
            allow_all_outbound=True,
            description="Allow ssh access to ec2 instances",
        )
        security_group.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(22),
            "Allow ssh access from the world",
        )
        security_group.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(8080),
            "Allow http access from the world",
        )

        # The actual Web EC2 Instance for the web server
        key_pair = ec2.KeyPair(
            self,
            f"{stack_name}-key-pair",
            key_pair_name=f"{stack_name}-key",
            type=ec2.KeyPairType.ED25519
        )
        web_server = ec2.Instance(
            self,
            f"{stack_name}-ec2",
            key_name=key_pair.key_pair_name,
            vpc=vpc,
            instance_type=ec2.InstanceType("t3.micro"),
            machine_image=ec2.MachineImage.latest_amazon_linux(
                generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
                cpu_type=ec2.AmazonLinuxCpuType.X86_64
            ),
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
            security_group=security_group,
            role=web_server_role
        )
        with open("cdk/assets/configure_amz_linux_sample_app.sh") as f:
            user_data = f.read()
            web_server.user_data.add_commands(user_data)

        # Output
        CfnOutput(
            self,
            f"{stack_name}-ip-address",
            value=web_server.instance_public_ip
        )
        CfnOutput(
            self,
            f"{stack_name}-instance-id",
            value=web_server.instance_id
        )
        CfnOutput(
            self,
            f"{stack_name}-key-name",
            value=key_pair.key_pair_name
        )
