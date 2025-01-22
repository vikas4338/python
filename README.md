## Launch EC2 Instance (LaunchEc2Instance.py)
We could use this automation to launch instances to save cost, like starting instance every morning based on some cloudwatch event.

## Payload to test
We could configure following parameters to run lambda function, which will help launching instance in particular region and the instance type we pass in payload

`json
{
  "region": "us-east-1",
  "image_id": "ami-0df8c184d5f6ae949",
  "instance_type": "t2.micro",
  "key_name": "my_key_pair_1",
  "numberOfInstances": 1
}
`

![image](https://github.com/user-attachments/assets/0cfaf699-f7a6-4fee-9149-6fc87edd5d77)
