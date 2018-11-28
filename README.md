# Scrapy games discount filter

This is a scrapy spider created to filter all games with a given discount or more.

## Requirements:

scrapy
python 3.x

## Usage:

Run in the root of the project:
```bash
scrapy crawl nuuvem -o output.json -a discount=80
```
You can change the name of the outpt file. If the discount parameter is ommited, the default discount filter will be 80%.
