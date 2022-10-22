<?php

$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://sandbox.api.visa.com/pav/v1/cardvalidation',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_SSL_VERIFYHOST => 2,
  CURLOPT_SSLVERSION => 1,
  CURLOPT_SSLCERT => getcwd()."/cert.pem",
  CURLOPT_SSLKEY => getcwd()."/privateKey.pem",
  CURLOPT_POSTFIELDS =>'{
    "cardCvv2Value": "999",
    "primaryAccountNumber": "4957030420210454",
    "cardExpiryDate": "2040-10",
    "acquiringBin": "408999",
    "acquirerCountryCode": "840"
}',
  CURLOPT_HTTPHEADER => array(
    'Authorization: Basic MDZaUFFFNE1aMlk5NjZYTk45VlAyMWsteXdxR29adDBnbmtZTGwtVTkxUHJ2dmo5ODp6SXVLcmwyZDMxWUh4MUUydjliVUhaY0NvMFF6',
    'Content-Type: application/json'
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
