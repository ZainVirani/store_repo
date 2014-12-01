#!/usr/loca/bin/perl
use CGI::Compile;
my $q = CGI::Compile->compile("./register.cgi");
use strict;

my $username = $q->param('username');
my $name = $q->param('name');
my $password = $q->param('password');
my @array = ("$name", "$username", "$password", "\n");
my $line = join(' , ', @array);


my $file = 'Members.csv';
open (FILE, '+>>$file') or die "Cannot open file";
my $inputLine = <INPUT>;
while($line = <INPUT>)
{
	if(index($line, "$username") != -1) {
	print "Content-type: text/html\n\n";
	print "<HTML>\n";
	print "<HEAD>\n";
	print "<TITLE> Error Page </TITLE> \n";
	print "</HEAD>\n";
	print "<BODY>\n";
	print "The username you have entered is already in use.";
	print "<br><a href=\"http//www.cs.mcgill.ca\">Home Page</a> \n";
	print "<br><a href=\"http://www.cs.mcgill.ca\">Registration Page</a> \n";
	print "</BODY>\n";
	close(FILE)
	}
	else {
#seeking to the end of the file to append
seek(PTR, 0, 2);
print PTR $line;
}
}
close(PTR);

