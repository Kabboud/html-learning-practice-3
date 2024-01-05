#!/usr/bin/perl
use CGI ':standard';
print "Content-type: text/html\n\n";

$fn = param ('first');
$ln = param ('last');
$g = param ('gender');
$streetnum = param ('number');
$streetname = param ('street');
$ct = param ('city');
$pc = param ('postal');
$province = param ('province');
$phone = param ('phone');
$email = param ('email');
$pass = param ('pass');

$error = 0;

if ($phone !~ m/^\d{10}$/){
	$error = 1;
	print "Phone Number is not properly formatted. Please go back and try again.<br>";
}
if ($email !~ m/.+@.*/){
	$error = 1;
	print "Email address is not properly formatted. Please go back and try again.<br>";
}
if ($pc !~ m/^.{6}$/){
	$error = 1;
	print "Postal Code is not of proper length. Please go back and try again.<br>";
}
if ($error eq 0){
	print "<body style='background-color: powderblue; text-align: center'>";
	print "<div style='font-family: cursive'>";
	print "<p>Hello $fn $ln from $province. <br>";
	print "You are a $g person living at the home address of $streetnum $streetname in the city of $ct at postal code $pc.<br>";
	print "Your email address is $email and your phone number is $phone.<br>";
	print "Your password is $pass.</p><br>";
	print "Thank you for registering with us!";
	print "</div></body>";
}