<?php
/* Smarty version 3.1.39, created on 2021-11-17 22:17:28
  from 'module:psfeaturedproductsviewste' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.39',
  'unifunc' => 'content_61957168a6fa83_32263178',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    'fa6cc378d2942c8857b89d6bca728048c0caeedd' => 
    array (
      0 => 'module:psfeaturedproductsviewste',
      1 => 1633363913,
      2 => 'module',
    ),
    '86a4d354f725902b1405db749b93834da03807f6' => 
    array (
      0 => '/var/www/html/themes/classic/templates/catalog/_partials/productlist.tpl',
      1 => 1633363913,
      2 => 'file',
    ),
    '4e48f9081812442e5797c9033049dad3e79d82e7' => 
    array (
      0 => '/var/www/html/themes/classic/templates/catalog/_partials/miniatures/product.tpl',
      1 => 1633363913,
      2 => 'file',
    ),
    '0724df70e9113f9ffcf0299fe2d091b4d46089e2' => 
    array (
      0 => '/var/www/html/themes/classic/templates/catalog/_partials/product-flags.tpl',
      1 => 1633363913,
      2 => 'file',
    ),
  ),
  'cache_lifetime' => 31536000,
),true)) {
function content_61957168a6fa83_32263178 (Smarty_Internal_Template $_smarty_tpl) {
?><section class="featured-products clearfix">
  <h2 class="h2 products-section-title text-uppercase">
    Popularne produkty
  </h2>
  <div class="products row">
            
<div class="product">
  <article class="product-miniature js-product-miniature" data-id-product="1" data-id-product-attribute="0">
    <div class="thumbnail-container">
      
                  <a href="https://localhost:8080/strona-glowna/1-darmowy-produkt.html" class="thumbnail product-thumbnail">
            <img
              src="https://localhost:8080/img/p/pl-default-home_default.jpg"
              loading="lazy"
              width="250"
              height="250"
            />
          </a>
              

      <div class="product-description">
        
                      <h3 class="h3 product-title"><a href="https://localhost:8080/strona-glowna/1-darmowy-produkt.html" content="https://localhost:8080/strona-glowna/1-darmowy-produkt.html">Darmowy Produkt</a></h3>
                  

        
                      <div class="product-price-and-shipping">
              
              

              <span class="price" aria-label="Cena">
                                                  0,00 zł
                              </span>

              

              
            </div>
                  

        
          
<div class="product-list-reviews" data-id="1" data-url="https://localhost:8080/module/productcomments/CommentGrade">
  <div class="grade-stars small-stars"></div>
  <div class="comments-nb"></div>
</div>


        
      </div>

      
    <ul class="product-flags js-product-flags">
                    <li class="product-flag new">Nowy produkt</li>
            </ul>


      <div class="highlighted-informations no-variants hidden-sm-down">
        
          <a class="quick-view js-quick-view" href="#" data-link-action="quickview">
            <i class="material-icons search">&#xE8B6;</i> Szybki podgląd
          </a>
        

        
                  
      </div>
    </div>
  </article>
</div>

    </div>  <a class="all-product-link float-xs-left float-md-right h4" href="https://localhost:8080/2-strona-glowna">
    Wszystkie produkty<i class="material-icons">&#xE315;</i>
  </a>
</section>
<?php }
}
