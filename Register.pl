#!/usr/bin/perl
#perl file for registration page
use CGI;
use CGI::Carp 'fatalsToBrowser';
my $q = CGI->new();
use strict;
use warnings;
#getting values from the HTML form
my $username = $q->param('username');
my $name = $q->param('name');
my $password = $q->param('password');
my $password1 = $q->param('password1');
my @array = ($name, $username, $password, " ");
my $line = join(',', @array);

print "Content-type: text/html\n\n";
my $file = 'Members.csv';
open(my $csv, '+<', $file) or die "Cannot open file";
my $inputLine = <$csv>;
my $found=0;
	if($password ne $password1){
	print "<HTML>\n";
	print "<HEAD>\n";
	print "<TITLE> Error Page </TITLE>\n";
	print "</HEAD>\n";
	print "<BODY>\n";
	print "<br><br><br><br>\n";
	print "<center><b> Your passwords have to match !!! Fail. </b></center>\n";
	print "<br><br><br><center><a href=\"register.html\"> Click here to go back to the registration page!</a></b></center> \n";
	print "</BODY>\n";
}
else{
#checking if username is already in use.
	while($inputLine =<$csv>){
		if(index($inputLine, $username) != -1){
			$found=1;
			print "<HTML>\n";
			print "<HEAD>\n";
			print "<TITLE> Error Page </TITLE>\n";
			print "</HEAD>\n";
			print "<BODY>\n";
			print "<br><br><br><br>\n";
			print "<center>The username you have entered is already in use.</center>";
			print "<br><center><a href=\"index.html\">Home Page</a></center< \n";
			print "<br><center><a href=\"register.html\">Registration Page</a></center> \n";
			print "</BODY>\n";
			close($csv);
		}
		if(eof){
			if($found==0){
				#seeking to the end of the file to append if username is not in use
				seek($csv, 0, 2);
				print $csv "$line\n";
				print "<HTML>\n";
				print "<HEAD>\n";
				print "<TITLE> Transfer Page </TITLE>\n";
				print "<BODY>\n";
				print "<br><br><br><br>\n";
				print "<b><center>Congratulations. You have made an account!</center></b>";
				print "<br><center><a href=\"login.html\">Click here to login.</center></a> \n";
				print "</BODY>\n";
				close($csv);
			}
		}
}
}

