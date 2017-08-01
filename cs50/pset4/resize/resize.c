/**
 * Copies a BMP piece by piece, just because.
 */
       
#include <stdio.h>
#include <stdlib.h>

#include "bmp.h"


int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 4)
    {
        fprintf(stderr, "Usage: ./resize infile outfile\n");
        return 1;
    }
    
    

    // remember filenames
    int scale = atoi(argv[1]);
    char *infile = argv[2];
    char *outfile = argv[3];
    
    if(scale>100 || scale<=0){
        printf("Please enter a positive scale factor less than or equal to 100\n");
    }
    
    // open input file 
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }

    // open output file
    FILE *outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 3;
    }

    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);
    
    int widthOriginal = bi.biWidth;
    
    // determine initial padding
    int paddingBefore =  (4 - (widthOriginal * sizeof(RGBTRIPLE)) % 4) % 4;
    
    //Adjust values in BITMAP Headers to appropriate scale
    
    bi.biWidth *= scale;
    bi.biHeight *= scale;
    // determine padding after scaling
    
    int paddingAfter =  (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;
    bi.biSizeImage = (((sizeof(RGBTRIPLE) * bi.biWidth) + paddingAfter) * abs(bi.biHeight));
    bf.bfSize = bi.biSizeImage +sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER);
    
    
    // establish the offset that we need to get back to the beginning of row as a long data type
    
    long offset = widthOriginal*sizeof(RGBTRIPLE) + paddingBefore;

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 || 
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 4;
    }

    // write outfile's BITMAPFILEHEADER
    fwrite(&bf, sizeof(BITMAPFILEHEADER), 1, outptr);

    // write outfile's BITMAPINFOHEADER
    fwrite(&bi, sizeof(BITMAPINFOHEADER), 1, outptr);

    // iterate over infile's scanlines
    for (int i = 0, biHeight = abs(bi.biHeight); i < biHeight; i++)
    {
        // iterate over pixels in scanline
            for (int j = 0; j < widthOriginal; j++){
            // temporary storage
            RGBTRIPLE triple;
            
            // read RGB triple from infile
            fread(&triple, sizeof(RGBTRIPLE), 1, inptr);
            
                // Write scale number of times 
                for(int k=0; k<scale; k++){
                    fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);
                    }
            }
            // skip over padding in the original
            fseek(inptr, paddingBefore, SEEK_CUR);
            
            // then add required padding for newly scaled image
            for (int k = 0; k < paddingAfter; k++){
            fputc(0x00, outptr);
            }
            
            if((i+1)%scale!=0){
                fseek(inptr, -offset, SEEK_CUR);
            }
        }

    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    // success
    return 0;
}
