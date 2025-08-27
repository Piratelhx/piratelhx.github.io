source "https://rubygems.org"

gem "jekyll", "~> 4.2"
gem "jekyll-paginate-v2"
gem "jekyll-feed", "~> 0.15.1"
gem "jekyll-seo-tag", "~> 2.7"
gem "jekyll-sitemap", "~> 1.4"
gem "webrick", "~> 1.7"
gem "tale"

group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.12"
  gem "jekyll-seo-tag"
  gem "jekyll-sitemap"
  gem "jekyll-paginate"
end

# Windows and JRuby does not include zoneinfo files
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

gem "wdm", "~> 0.1", :platforms => [:mingw, :x64_mingw, :mswin]
gem "http_parser.rb", "~> 0.6.0", :platforms => [:jruby]
