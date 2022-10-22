<?php

/**
 * (c) Copyright 2018 - 2020 Visa. All Rights Reserved.**
 *
 * NOTICE: The software and accompanying information and documentation (together, the “Software”) remain the property of and are proprietary to Visa and its suppliers and affiliates. The Software remains protected by intellectual property rights and may be covered by U.S. and foreign patents or patent applications. The Software is licensed and not sold.*
 *
 *  By accessing the Software you are agreeing to Visa's terms of use (developer.visa.com/terms) and privacy policy (developer.visa.com/privacy).In addition, all permissible uses of the Software must be in support of Visa products, programs and services provided through the Visa Developer Program (VDP) platform only (developer.visa.com). **THE SOFTWARE AND ANY ASSOCIATED INFORMATION OR DOCUMENTATION IS PROVIDED ON AN “AS IS,” “AS AVAILABLE,” “WITH ALL FAULTS” BASIS WITHOUT WARRANTY OR  CONDITION OF ANY KIND. YOUR USE IS AT YOUR OWN RISK.** All brand names are the property of their respective owners, used for identification purposes only, and do not imply product endorsement or affiliation with Visa. Any links to third party sites are for your information only and equally  do not constitute a Visa endorsement. Visa has no insight into and control over third party content and code and disclaims all liability for any such components, including continued availability and functionality. Benefits depend on implementation details and business factors and coding steps shown are exemplary only and do not reflect all necessary elements for the described capabilities. Capabilities and features are subject to Visa’s terms and conditions and may require development,implementation and resources by you based on your business and operational details. Please refer to the specific API documentation for details on the requirements, eligibility and geographic availability.*
 *
 * This Software includes programs, concepts and details under continuing development by Visa. Any Visa features,functionality, implementation, branding, and schedules may be amended, updated or canceled at Visa’s discretion.The timing of widespread availability of programs and functionality is also subject to a number of factors outside Visa’s control,including but not limited to deployment of necessary infrastructure by issuers, acquirers, merchants and mobile device manufacturers.*
 *
 */

$url = 'https://sandbox.api.visa.com/vdp/helloworld';

// THIS IS EXAMPLE ONLY how will user_id and password look like
// userId = "1WM2TT4IHPXC8DQ5I3CH21n1rEBGK-Eyv_oLdzE2VZpDqRn_U";
// password = "19JRVdej9";
$username = '06ZPQE4MZ2Y966XNN9VP21k-ywqGoZt0gnkYLl-U91Prvvj98';
$password = 'zIuKrl2d31YHx1E2v9bUHZcCo0Qz';

# THIS IS EXAMPLE ONLY how will cert and key look like
# cert = 'cert.pem'
# key = 'key_83d11ea6-a22d-4e52-b310-e0558816727d.pem'

$cert = getcwd()."/cert.pem";
$key = getcwd()."/visa Certificate Private Key.pem";

$curl = curl_init();

curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);

curl_setopt($curl, CURLOPT_PORT, 443);
curl_setopt($curl, CURLOPT_VERBOSE, 1);
curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, 2);
curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, 2);
curl_setopt($curl, CURLOPT_SSLVERSION, 1);
curl_setopt($curl, CURLOPT_SSLCERT, $cert);
curl_setopt($curl, CURLOPT_SSLKEY, $key);

curl_setopt($curl, CURLOPT_HTTPAUTH, CURLAUTH_BASIC);
curl_setopt($curl, CURLOPT_USERPWD, "$username:$password");

curl_setopt($curl, CURLOPT_URL, $url);

$response = curl_exec($curl);

$response_info = curl_getinfo($curl);

if ($response_info['http_code'] === 0) {
    $curl_error_message = curl_error($curl);

    // curl_exec can sometimes fail but still return a blank message from curl_error().
    if (!empty($curl_error_message)) {
        $error_message = "API call to $url failed: $curl_error_message";
    } else {
        $error_message = "API call to $url failed, but for an unknown reason. " .
            "This could happen if you are disconnected from the network.";
    }
    echo $error_message;
} elseif ($response_info['http_code'] >= 200 && $response_info['http_code'] <= 299) {
    echo "Your call returned with a success code - " . $response_info['http_code'] . "";
    echo "Json Response: $response";
} else {
    echo "[HTTP Status: " . $response_info['http_code'] . "]\n[" . $response . "]";
    echo "\nError connecting to the API ($url)";
}
