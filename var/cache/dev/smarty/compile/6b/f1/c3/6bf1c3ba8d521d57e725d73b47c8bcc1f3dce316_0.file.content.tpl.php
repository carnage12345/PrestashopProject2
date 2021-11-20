<?php
/* Smarty version 3.1.39, created on 2021-11-19 23:27:34
  from '/var/www/html2/_admin/themes/new-theme/template/content.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.39',
  'unifunc' => 'content_619824d6cd9140_04111901',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '6bf1c3ba8d521d57e725d73b47c8bcc1f3dce316' => 
    array (
      0 => '/var/www/html2/_admin/themes/new-theme/template/content.tpl',
      1 => 1637337245,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_619824d6cd9140_04111901 (Smarty_Internal_Template $_smarty_tpl) {
?>
<div id="ajax_confirmation" class="alert alert-success" style="display: none;"></div>


<?php if ((isset($_smarty_tpl->tpl_vars['content']->value))) {?>
  <?php echo $_smarty_tpl->tpl_vars['content']->value;?>

<?php }
}
}
