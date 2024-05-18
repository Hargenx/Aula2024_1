package com.poo_2024_final.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;
import org.springframework.orm.jpa.LocalContainerEntityManagerFactoryBean;
import org.springframework.orm.jpa.vendor.HibernateJpaVendorAdapter;

@Configuration
@EnableJpaRepositories(basePackages = "com.aula2024.poo_2024_final.repository")
public class JpaConfig {

    @Bean
    public LocalContainerEntityManagerFactoryBean entityManagerFactory() {
        LocalContainerEntityManagerFactoryBean emfb = new LocalContainerEntityManagerFactoryBean();
        emfb.setJpaVendorAdapter(new HibernateJpaVendorAdapter());
        emfb.setPackagesToScan("com.aula2024.poo_2024_final.model");
        return emfb;
    }
}
