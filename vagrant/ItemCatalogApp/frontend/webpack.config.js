const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
    mode: 'development', //change this value to production when the project is completed
    entry: {
        //js
        main: './src/main.js',
        dialog: '/src/components/dialog.js',
        //css
        styles: '/src/styles/styles.css',
    },
    output: {
        filename: 'js/[name].js',
        path: path.resolve(__dirname, 'static'),
    },
    module: {
        rules:[
            {
                test:/\.css$/,
                use:[
                    MiniCssExtractPlugin.loader,
                    'css-loader',
                ],
            }
        ],
    },
    plugins:[
        // Output CSS files to 'static/css'
        new MiniCssExtractPlugin({filename:'css/[name].css',}),
    ],
    resolve:{
        alias: {
            'bcryptjs': 'bcryptjs/dist/bcrypt.js'
        },
    },
};