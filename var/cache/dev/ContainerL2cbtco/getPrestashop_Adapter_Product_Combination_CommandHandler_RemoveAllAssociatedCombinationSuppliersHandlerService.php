<?php

use Symfony\Component\DependencyInjection\Argument\RewindableGenerator;

// This file has been auto-generated by the Symfony Dependency Injection Component for internal use.
// Returns the public 'prestashop.adapter.product.combination.command_handler.remove_all_associated_combination_suppliers_handler' shared service.

return $this->services['prestashop.adapter.product.combination.command_handler.remove_all_associated_combination_suppliers_handler'] = new \PrestaShop\PrestaShop\Adapter\Product\Combination\CommandHandler\RemoveAllAssociatedCombinationSuppliersHandler(${($_ = isset($this->services['prestashop.adapter.product.update.product_supplier_updater']) ? $this->services['prestashop.adapter.product.update.product_supplier_updater'] : $this->load('getPrestashop_Adapter_Product_Update_ProductSupplierUpdaterService.php')) && false ?: '_'});