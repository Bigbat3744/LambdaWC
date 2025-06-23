# Word Count Lambda Function

This project contains an AWS Lambda function that counts the number of words in a text file uploaded to an S3 bucket and sends the result via email using Amazon SNS.

## Project Structure

```
lambda-word-count
├── src
│   ├── lambda_function.py       # Main Lambda function triggered by S3 events
│   └── utils
│       └── word_counter.py       # Utility function to count words
├── requirements.txt              # Project dependencies
├── event.json                    # Sample event for local testing
└── README.md                     # Project documentation
```

## Setup Instructions

1. **AWS Account**: Ensure you have an AWS account with permissions to create Lambda functions, S3 buckets, and SNS topics.

2. **Create an S3 Bucket**: Create an S3 bucket where you will upload text files.

3. **Create an SNS Topic**: Create an SNS topic to which the Lambda function will publish the word count results. Subscribe your email address to this topic to receive notifications.

4. **IAM Role**: Assign the `LambdaAccessRole` to your Lambda function to allow it to access S3 and SNS services.

5. **Deploy the Lambda Function**:
   - Navigate to the AWS Lambda console.
   - Create a new Lambda function and upload the code from the `src` directory.
   - Set the trigger to the S3 bucket you created.

6. **Install Dependencies**: Use the `requirements.txt` file to install necessary dependencies. You can do this by running:
   ```
   pip install -r requirements.txt
   ```

## Usage

- Upload a text file to the configured S3 bucket.
- The Lambda function will be triggered automatically.
- You will receive an email with the word count of the uploaded file.

## Lambda Function Configuration

- The Lambda function is triggered by S3 events.
- It reads the content of the uploaded text file, counts the words using the `count_words` function from `word_counter.py`, and publishes the result to the SNS topic.

## Testing

- Use the `event.json` file to simulate an S3 file upload event for local testing of the Lambda function.

## License

This project is licensed under the MIT License.