

1. **Maldet**--- Malware scanner. Look into
     1. how we to add signatures to it and
     1. anything we can do to improve its functionality. Right now it runs every 24 hours and scans files modified in the last 7 days I believe.

1. **Wordpress Core + Plugin Vulnerabilities**.
     1. [x] Get on the mailing lists for vulnerabilities for Wordpress core
     1. and also for popular plugins such as Yoast (SEO) for example.

1. Little bit of **Ansible**. We use this for code deployments.

1. **WP command line**. Very handy and it will look good if you know how to use it.  http://wp-cli.org/

1. **strace PHP**
     1. [x] [strace PHP](https://serverfault.com/questions/144912/how-can-i-tell-which-page-is-creating-a-high-cpu-load-httpd-process). This command is from Media Temple:

```
strace php5 index.php 2>&1 | perl -ne 'if (/plugins\/([\w\d-_]*)/ ) { print "$1\n" }' | sort | uniq -c | sort -n
```

1. **Securing WordPress**
     1. [x] WordPress Essential Training: [Is WordPress safe and secure?](https://www.linkedin.com/learning/wordpress-essential-training/is-wordpress-safe-and-secure), etc.
     1. WordPress: [Developing Secure Sites](https://www.linkedin.com/learning/wordpress-developing-secure-sites)
     1. WordPress Plugin Development: [Develop secure WordPress plugins](https://www.linkedin.com/learning/wordpress-plugin-development/develop-secure-wordpress-plugins)
     1. WordPress: Understanding Custom Plugins with PHP: [Securing your plugin](https://www.linkedin.com/learning/wordpress-understanding-custom-plugins-with-php/securing-your-plugin)

1. **AWS**
     1. **EC2**
     1. **RDS**
          1. data at rest encryption for [RDS](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html)
     1. **EBS**
          1. [Amazon EBS Encryption](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html)
     1. **S3**
           1. [Protecting Data Using Server-Side Encryption](http://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html)
     1. **AWS Shield**
           1. [DDOS Protection provided by AWS](https://aws.amazon.com/shield/).... We use some lower tier plan, but it would be good to just get up to speed on what Amazon is using and offering.
     1. **AWS WAF**
          1. [Use AWS WAF to Mitigate OWASP’s Top 10](https://d0.awsstatic.com/whitepapers/Security/aws-waf-owasp.pdf)
          1. [AWS WAF Management Console](https://console.aws.amazon.com/waf)
          1. [What Is AWS WAF and AWS Shield?](http://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html)
     1. See notes from AppSec California.


1. **Phpmyadmin**

1. **Miscellaneous**
     1. [x] [chroot User Separation](https://help.ubuntu.com/community/BasicChroot)
     1. [x] [.htaccess Rules](https://premium.wpmudev.org/blog/htaccess/) and [x] [Order](https://stackoverflow.com/questions/9943042/htaccess-order-deny-allow-deny)
     1. [x] [Nginx vs Apache](https://support.pagely.com/hc/en-us/articles/115000020792-Your-guide-to-Pagely-s-NGINX-Apache-and-NGINX-only-modes)
