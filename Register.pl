#!/usr/loca/bin/perl
use CGI;
my $q = CGI->new();
use strict;

my $username = $q->param('username');
my $name = $q->param('name');
my $password = $q->param('password');
my @array = ($name, $username, $password, "\r");
my $line = join(' , ', @array);

print "Content-type:text/html\n\n";
my $file = 'Members.csv';
open (FILE, '+>>$file') or die "Cannot open file";
my $inputLine = <FILE>;
while($inputLine = <FILE>)
{
	if(index($line, $username) != 4){
	print "<HTML>\n";
	print "<HEAD>\n";
	print "<TITLE> Error Page </TITLE> \n";
	print "</HEAD>\n";
	print "<BODY>\n";
	print "The username you have entered is already in use.";
	print "<br><a href=\"index.html\">Home Page</a> \n";
	print "<br><a href=\"register.html\">Registration Page</a> \n";
	print "</BODY>\n";
	close(FILE);
	}
	else {
#seeking to the end of the file to append
seek(FILE, 0, 2);
print FILE $line;
}
}
close(FILE);

