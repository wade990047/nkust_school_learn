<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the web site, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'wpadmin' );

/** Database username */
define( 'DB_USER', 'root' );

/** Database password */
define( 'DB_PASSWORD', '20040415' );

/** Database hostname */
define( 'DB_HOST', 'localhost' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         'wD)u],My3kkEK5geWN3f|+0bt#x3/.EVhGC!.P=8nvFkR7}nf-d%Fb?+5K,*o9>.' );
define( 'SECURE_AUTH_KEY',  'CR4L2#o-XYM5*ww^{!B]%@v,<`9SY`*)#3B04j^{Q r37@o;J(IzU;8;3$&0.a3e' );
define( 'LOGGED_IN_KEY',    'n!)Mw?>Q>Wmz9blI~Aq=&3B.bOL]-_2)!:iLVyrvb:^&Eb$|7m7_UX93#jD&)wFo' );
define( 'NONCE_KEY',        '#o&Kl[t6EVW.-wI%1$gGZPh&O5M}OXLJd>xF6A|L[!@HZhoBuC)xyMSkTI9y>ja ' );
define( 'AUTH_SALT',        '9RQJ^!]Ibdv}E$/i<%~HQnTLstgvyg$`BO~xd- ]l5}YNIMTeanFt#f971<$o?+V' );
define( 'SECURE_AUTH_SALT', ']]sHhnX;!RBVnu[6s2J8]2TtH0EM}DK%_{Z0,>jk| 2y.hm:TxqMGz7mdX4eEZ|~' );
define( 'LOGGED_IN_SALT',   'U8^PVUJQCb1yvmWA,l<_FsRO)?Qcy{CiLtefiU]Yg{Pj*m32_#Jm$H TBva4YO^g' );
define( 'NONCE_SALT',       '-5Tb;ftrZ8mqJF!Mr,ZwzrI;AUp7MNk|+i5d3_GKPRW`%]=*wd EC7ej[^PN@0T^' );

/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
define( 'WP_DEBUG', false );

/* Add any custom values between this line and the "stop editing" line. */



/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
