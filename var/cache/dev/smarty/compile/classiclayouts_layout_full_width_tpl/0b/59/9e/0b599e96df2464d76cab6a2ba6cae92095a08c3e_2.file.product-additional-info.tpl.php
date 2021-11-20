<?php
/* Smarty version 3.1.39, created on 2021-11-19 23:38:06
  from '/var/www/html2/themes/classic/templates/catalog/_partials/product-additional-info.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.39',
  'unifunc' => 'content_6198274e84d4d5_02853928',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '0b599e96df2464d76cab6a2ba6cae92095a08c3e' => 
    array (
      0 => '/var/www/html2/themes/classic/templates/catalog/_partials/product-additional-info.tpl',
      1 => 1637337249,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_6198274e84d4d5_02853928 (Smarty_Internal_Template $_smarty_tpl) {
?><div class="product-additional-info js-product-additional-info">
  <?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['hook'][0], array( array('h'=>'displayProductAdditionalInfo','product'=>$_smarty_tpl->tpl_vars['product']->value),$_smarty_tpl ) );?>

</div>
<?php }
}
