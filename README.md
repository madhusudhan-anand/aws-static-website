# Static Website Hosting on AWS

This project hosts a static website using Amazon S3 for storage and CloudFront as a CDN for faster content delivery. It includes a simple `index.html` page and associated CSS. CloudFront acts as a content delivery network (CDN) to improve loading speeds by serving content from locations closer to users, while CloudFront's Origin Access Control (OAC) ensures secure access to the S3 bucket.

## Technologies Used

- **Amazon S3**: Used for storage and serving the website content.
- **Amazon CloudFront**: Acts as a content delivery network (CDN) to accelerate content delivery globally.
- **HTML**: The structure of the website (`index.html`).
- **CSS**: The styling of the website.

## Features

- **Static Website**: The website is fully static, consisting of HTML and CSS files.
- **Optimized Performance**: Content is served globally via CloudFront, ensuring faster load times regardless of the user's location.
- **Secure Access**: CloudFront's Origin Access Control (OAC) ensures secure access to the S3 bucket.
- **Minimal Setup**: The website is hosted with minimal AWS resources, ensuring cost efficiency.

## How to Deploy

1. **Create an S3 Bucket**:
   - Go to the AWS S3 console and create a new bucket to store your website files.
   - Enable static website hosting for the bucket.
   
2. **Upload Your Website Files**:
   - Upload `index.html` and `style.css` to your S3 bucket.

3. **Set Up CloudFront Distribution**:
   - Create a CloudFront distribution and link it to the S3 bucket.
   - Set the S3 bucket as the origin for the CloudFront distribution.

4. **Configure CloudFront Origin Access Control (OAC)**:
   - Enable OAC to ensure that CloudFront is the only entity with access to the S3 bucket.

5. **Update DNS Settings** (Optional):
   - If using a custom domain, update the DNS settings to point to CloudFront's distribution URL.

## License

This project does not include a specific license.
