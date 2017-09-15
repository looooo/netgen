#ifndef FILE_MYDEFS
#define FILE_MYDEFS

/**************************************************************************/
/* File:   mydefs.hh                                                      */
/* Author: Joachim Schoeberl                                              */
/* Date:   10. Mar. 98                                                    */
/**************************************************************************/

#define PACKAGE_VERSION "6.2-dev"

/*
  defines for graphics, testmodes, ...
*/


// #define DEBUG

#ifdef WIN32
   #if NGINTERFACE_EXPORTS || NGLIB_EXPORTS || nglib_EXPORTS
      #define DLL_HEADER   __declspec(dllexport)
   #else
      #define DLL_HEADER   __declspec(dllimport)
   #endif
#else
   #if __GNUC__ >= 4
      #define DLL_HEADER __attribute__ ((visibility ("default")))
   #else
      #define DLL_HEADER
   #endif
#endif




#ifndef __assume
#ifdef __GNUC__
#define __assume(cond) if (!(cond)) __builtin_unreachable(); else;
#else
#define __assume(cond)
#endif
#endif


#ifndef NG_INLINE
#ifdef __INTEL_COMPILER
#ifdef WIN32
#define NG_INLINE __forceinline inline
#else
#define NG_INLINE __forceinline inline
#endif
#else
#ifdef __GNUC__
#define NG_INLINE __attribute__ ((__always_inline__)) inline
#define VLA
#else
#define NG_INLINE inline
#endif
#endif
#endif


// #define BASE0
// #define DEBUG


#define noDEMOVERSION
#define noDEVELOP
#define noSTEP
#define noSOLIDGEOM

#define noDEMOAPP
#define noMODELLER

#define noSTAT_STREAM
#define noLOG_STREAM

#endif
