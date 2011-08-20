#!/usr/bin/perl
use strict;
use Web::Scraper;
use URI;
use Encode;
use utf8;
use CGI;
use CGI::Carp qw(fatalsToBrowser);

my $cgi = new CGI;
$cgi->charset('utf-8');

print $cgi->header;
print $cgi->start_html(-title=>'しいじいあい', -lang=> 'ja-JP');
print "hello!";
print $cgi->end_html;

=pod comment
my $uri = URI->new("http://www.mai-net.net/bbs/sst/sst.php?act=list");
my $scraper = scraper {
    process '//table[@class="brdr"]/tr[position() >= 3]/td|//table[@class="brdr"]/tr[2]/td[not(position() < last() - 5 or position() > last())]','list[]' => 'TEXT';
};
my $result = $scraper->scrape($uri);
=cut


