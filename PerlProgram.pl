#!/usr/loca/bin/perl
use CGI
use strict;

my $username = param('username');
my $name = param('name');
my $password = param('password');
my @array = ("$name", "$username", "$password");
my $line = join(' , ', @array);


$file = 'Members.csv'
open(FILE, '+>>$file') or die "Cannot open file";
my $inputLine = <INPUT>;
while($line = <INPUT>)
{
	if(index($line, "$username") != -1) {
	#Link to error HTML page
	close(FILE)
	}
	else {
#seeking to the end of the file to append
seek(PTR, 0, 2);
print PTR $line;
}
}
close(PTR);

