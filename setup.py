import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="route53_cdk_dyndns",
    version="0.0.1",

    description="An empty CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "route53_cdk_dyndns"},
    packages=setuptools.find_packages(where="route53_cdk_dyndns"),

    install_requires=[
        "aws-cdk-lib>=2.0.0",
        "constructs>=10.0.0",
        "aws-cdk.aws-codestar-alpha>=2.0.0alpha1",
        "requests==2.21.0",
    ],

    python_requires=">=3.7",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
