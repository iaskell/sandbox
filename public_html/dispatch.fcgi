#!/usr/bin/env /usr/bin/perl
use strict;
use warnings;
use utf8;

use CGI::Fast;
use CGI::Carp qw(fatalsToBrowser);

my $scriptrootpath='../scripts';
while (my $q = CGI::Fast->new()){
	if( -f "$scriptrootpath$ENV{'PATH_INFO'}" ){
		do "$scriptrootpath$ENV{'PATH_INFO'}";
	}else{
		print "Status: 404 Not Found\n";
	}
};
