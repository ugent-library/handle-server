#!/usr/bin/env perl

use Catmandu::Sane;
use Catmandu::Util qw(:is);
use DBI;

# Purpose: exports handles out of mysql, and create postgres import file

my $dbh = DBI->connect(
    "dbi:mysql:dbname=handle",
    "handle",
    "handle"
) or die($DBI::errstr);

# refs: always NULL
print <<EOF;
INSERT INTO handles(handle,idx,type,data,ttl,ttl_type,timestamp,admin_read,admin_write,pub_read,pub_write)
VALUES
EOF

my $sth = $dbh->prepare(qq(SELECT * FROM handles))
    or die($dbh->errstr);

$sth->execute();

my $has_prev_row = 0;
while (my $row = $sth->fetchrow_hashref()) {
    print ",\n" if $has_prev_row;
    print "(";

    my @r = ();
    push @r, is_string($row->{handle}) ? "'$row->{handle}'" : "''";
    push @r, is_natural($row->{idx}) ? "$row->{idx}" : "0";
    push @r, is_string($row->{type}) ? "'$row->{type}'" : "''";
    push @r, is_string($row->{data}) ? "'$row->{data}'::bytea" : "''::bytea";
    push @r, $row->{ttl};
    push @r, $row->{ttl_type};
    push @r, $row->{timestamp};
    push @r, $row->{admin_read} ? "true": "false";
    push @r, $row->{admin_write} ? "true": "false";
    push @r, $row->{pub_read} ? "true": "false";
    push @r, $row->{pub_write} ? "true": "false";
    print join(",", @r);

    print ")";
    $has_prev_row = 1;
}

print ";";

$sth->finish;


$dbh->disconnect;
