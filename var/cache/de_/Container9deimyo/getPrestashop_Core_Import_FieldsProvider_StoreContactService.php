<?php

use Symfony\Component\DependencyInjection\Argument\RewindableGenerator;

// This file has been auto-generated by the Symfony Dependency Injection Component for internal use.
// Returns the public 'prestashop.core.import.fields_provider.store_contact' shared service.

return $this->services['prestashop.core.import.fields_provider.store_contact'] = new \PrestaShop\PrestaShop\Core\Import\EntityField\Provider\StoreContactFieldsProvider(${($_ = isset($this->services['translator']) ? $this->services['translator'] : $this->getTranslatorService()) && false ?: '_'});