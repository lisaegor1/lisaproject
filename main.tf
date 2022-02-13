provider "aws" {
  shared_credentials_file = "creds"
  region                  = "eu-north-1"
}

resource "aws_eip" "my_static_ip" {
  instance = aws_instance.WebServer.id #static ip
}

resource "aws_instance" "WebServer" {
  ami                    = "ami-0bd9c26722573e69b"
  instance_type          = "t3.micro"
  vpc_security_group_ids = [aws_security_group.webserver.id]
  user_data              = file("user_data.sh") # or <<EOF ... EOF
  tags = {
    Name = "WebServerApache2"
  }

  lifecycle {
    create_before_destroy = true #Create new sserver --> Destroy old one
    /*
    lifecycle {
      prevent_destroy = true   # against accidental destruction
      ignore_changes = ["ami", "user_data"]   #ignore updates/changes to prevent suddenly destroy
    }
    */
  }
}

resource "aws_security_group" "webserver" {
  name        = "SG_WebServer"
  description = "SG for web"

  ingress {
    from_port   = 81
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "SG_for_Web"
  }
}

output "Webserver_id" {
  value = aws_instance.WebServer.id #show the instance id
}

output "eip_instance" {
  value = aws_eip.my_static_ip.public_ip #show eip of the instance
}
#Create new file outputs.tf for outputs
