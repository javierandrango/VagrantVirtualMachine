const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
    mode: 'development', //change this value to production when the project is completed
    entry: {
        //js
        main: './src/main.js',
        dialog: './src/components/dialog.js',
        //css
        styles: './src/styles/styles.css',
        //images
        icons: './src/icons/iconsIndex.js',
        images: './src/images/imagesIndex.js',
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
            },
            {
                test: /\.svg$/,
                use: [
                    {
                        loader: 'file-loader',
                        options: {
                            name: '[name].[ext]',
                            outputPath: '../static/icons',
                        },
                    },
                ],
            },
            {
                test: /\.(png|gif|jpg)$/,
                use: [
                    {
                        loader: 'file-loader',
                        options: {
                            name: '[name].[ext]',
                            outputPath: '../static/images',
                        },
                    },
                ],
            },
        ],
    },
    plugins:[
        // Output CSS files to 'static/css'
        new MiniCssExtractPlugin({filename:'css/[name].css',}),
    ],
    resolve:{
        fallback:{"crypto":false},
        alias: {
            'bcryptjs': 'bcryptjs/dist/bcrypt.js'
        },
    },
};
