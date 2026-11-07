import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang4_p3_b2_c4_ds10(self):
                # Khai báo biến
                lisdang=['1']
                dang=random.choice(lisdang)
                if dang=='1':
                    x=symbols('x')
                    a=randint(2,6)
                    b=1
                    lisc=[20,30,40,50]
                    c=random.choice(lisc)
                    d=randint(2,5)
                    hsb=Rational(4*b-4*a,c)
                    hsa=-Rational(4*b-4*a,c**2)
                    hsc=a
                    f=hsa*x**2+hsb*x+hsc
                    r=Rational(c,12)
                    f0=hsc
                    f1=hsa*(1*r)**2+hsb*(1*r)+hsc
                    f2=hsa*(2*r)**2+hsb*(2*r)+hsc
                    f3=hsa*(3*r)**2+hsb*(3*r)+hsc
                    f4=hsa*(4*r)**2+hsb*(4*r)+hsc
                    f5=hsa*(5*r)**2+hsb*(5*r)+hsc
                    f6=hsa*(6*r)**2+hsb*(6*r)+hsc
                    f7=hsa*(7*r)**2+hsb*(7*r)+hsc
                    f8=hsa*(8*r)**2+hsb*(8*r)+hsc
                    f9=hsa*(9*r)**2+hsb*(9*r)+hsc
                    f10=hsa*(10*r)**2+hsb*(10*r)+hsc
                    f11=hsa*(11*r)**2+hsb*(11*r)+hsc
                    f12=hsa*(12*r)**2+hsb*(12*r)+hsc

                    kq1=f0+f1+f2+f3+f4+f5+f6+f7+f8+f9+f10+f11+f12
                    kq=kq1*(1+Rational(d,100))
                    while kq>9999:
                        x=symbols('x')
                        a=randint(2,6)
                        b=1
                        lisc=[20,30,40,50]
                        c=random.choice(lisc)
                        d=randint(2,5)
                        hsb=Rational(4*b-4*a,c)
                        hsa=-Rational(4*b-4*a,c**2)
                        hsc=a
                        f=hsa*x**2+hsb*x+hsc
                        r=Rational(c,12)
                        f0=hsc
                        f1=hsa*(1*r)**2+hsb*(1*r)+hsc
                        f2=hsa*(2*r)**2+hsb*(2*r)+hsc
                        f3=hsa*(3*r)**2+hsb*(3*r)+hsc
                        f4=hsa*(4*r)**2+hsb*(4*r)+hsc
                        f5=hsa*(5*r)**2+hsb*(5*r)+hsc
                        f6=hsa*(6*r)**2+hsb*(6*r)+hsc
                        f7=hsa*(7*r)**2+hsb*(7*r)+hsc
                        f8=hsa*(8*r)**2+hsb*(8*r)+hsc
                        f9=hsa*(9*r)**2+hsb*(9*r)+hsc
                        f10=hsa*(10*r)**2+hsb*(10*r)+hsc
                        f11=hsa*(11*r)**2+hsb*(11*r)+hsc
                        f12=hsa*(12*r)**2+hsb*(12*r)+hsc
                    
                        kq1=f0+f1+f2+f3+f4+f5+f6+f7+f8+f9+f10+f11+f12
                        kq=2*kq1*(1+Rational(d,100))        
                    
                    h1=kq   
                    number = Decimal(float(h1))  # Số cần làm tròn
                    kqz = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                    
                    # Nội dung câu hỏi
                    noidungcauhoi = ('Chiếc cầu dây văng một nhịp được thiết kế hai bên thành cầu có dạng parabol và được cố định bằng các dây cáp song song như hình vẽ'
                                    r'''\begin{center}
	\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
	\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 235; green, 235; blue, 210 }  ,fill opacity=1 ] (246.89,103.91) -- (292.12,114.63) -- (291.02,117.57) -- (245.79,106.84) -- cycle ;
	\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 235; green, 235; blue, 210 }  ,fill opacity=1 ] (227.62,114.58) -- (272.85,125.31) -- (271.74,128.24) -- (226.52,117.52) -- cycle ;
	\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 235; green, 235; blue, 210 }  ,fill opacity=1 ] (59.73,130.92) -- (63.39,49.82) -- (68.28,49.82) -- (71.94,130.92) -- cycle ;
	\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 235; green, 235; blue, 210 }  ,fill opacity=1 ] (46.97,123.95) -- (92.9,115.34) -- (93.78,118.33) -- (47.85,126.94) -- cycle ;
	\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 235; green, 235; blue, 210 }  ,fill opacity=1 ] (285.15,130.92) -- (288.82,49.82) -- (293.71,49.82) -- (297.37,130.92) -- cycle ;
	\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 235; green, 235; blue, 210 }  ,fill opacity=1 ] (34.01,103.36) -- (318.1,103.06) -- (318.1,105.85) -- (34.02,106.15) -- cycle ;
	\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 128; green, 128; blue, 128 }  ,fill opacity=1 ] (318.44,105.12) -- (306.46,116.41) -- (10.8,118.6) -- (35.1,104.78) -- cycle ;
	\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 235; green, 235; blue, 210 }  ,fill opacity=1 ] (10.8,116.41) -- (306.46,116.41) -- (306.46,118.6) -- (10.8,118.6) -- cycle ;
	\draw [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ] [dash pattern={on 4.5pt off 4.5pt}]  (22.95,111.69) -- (311.25,110.89) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ]   (158.16,116.58) -- (158.16,107.51) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ]   (171.92,102.89) -- (171.92,94.34) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ]   (216.02,116.41) -- (216.02,94.51) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ]   (177.3,116.58) -- (177.3,105.8) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ]   (196.02,116.41) -- (196.02,101.53) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ]   (234.95,116.24) -- (234.95,85.95) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ]   (251.73,116.24) -- (251.73,74.66) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ]   (101.8,116.24) -- (101.8,97.42) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ]   (120.95,116.75) -- (120.95,103.75) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ]   (138.8,116.41) -- (138.8,107) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ]   (82.87,116.24) -- (82.87,88.35) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ]   (65.66,116.24) -- (65.66,75.69) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ]   (223.33,102.89) -- (223.33,87.49) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ]   (265.06,116.24) -- (265.06,63.71) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ]   (52.54,115.73) -- (52.54,63.71) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ]   (204.41,102.89) -- (204.41,91.77) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ]   (188.92,102.89) -- (188.92,94.17) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ]   (240.33,102.55) -- (240.33,81.34) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ]   (258.83,102.89) -- (258.83,72.61) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ]   (285.07,102.38) -- (285.07,53.62) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ]   (122.24,103.06) -- (122.24,84.93) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ]   (139.44,102.55) -- (139.44,90.23) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ]   (155.15,102.72) -- (155.15,93.31) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ]   (106.53,102.89) -- (106.53,78.08) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ]   (89.33,102.89) -- (89.33,67.82) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ]   (72.12,102.89) -- (72.12,53.62) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][line width=1]    (68.28,49.82) .. controls (153.7,132.84) and (264.25,79.73) .. (288.39,49.82) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][line width=1]    (48.92,59.4) .. controls (132.6,150.9) and (244.89,89.31) .. (269.03,59.4) ;
	\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 235; green, 235; blue, 210 }  ,fill opacity=1 ] (40.37,140.5) -- (44.03,59.4) -- (48.92,59.4) -- (52.59,140.5) -- cycle ;
	\draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][fill={rgb, 255:red, 235; green, 235; blue, 210 }  ,fill opacity=1 ] (265.8,139.71) -- (269.46,58.61) -- (274.35,58.61) -- (278.01,139.71) -- cycle ;
	\draw  [draw opacity=0][fill={rgb, 255:red, 235; green, 235; blue, 210 }  ,fill opacity=1 ] (52.67,139.53) .. controls (52.67,139.54) and (52.67,139.54) .. (52.67,139.54) .. controls (52.67,141.21) and (49.91,142.55) .. (46.52,142.55) .. controls (43.27,142.55) and (40.62,141.33) .. (40.38,139.77) -- (46.52,139.54) -- cycle ; \draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ] (52.67,139.53) .. controls (52.67,139.54) and (52.67,139.54) .. (52.67,139.54) .. controls (52.67,141.21) and (49.91,142.55) .. (46.52,142.55) .. controls (43.27,142.55) and (40.62,141.33) .. (40.38,139.77) ;  
	\draw  [draw opacity=0][fill={rgb, 255:red, 235; green, 235; blue, 210 }  ,fill opacity=1 ] (71.94,130.23) .. controls (71.94,130.24) and (71.94,130.24) .. (71.94,130.24) .. controls (71.94,131.91) and (69.19,133.25) .. (65.79,133.25) .. controls (62.55,133.25) and (59.89,132.03) .. (59.65,130.47) -- (65.79,130.24) -- cycle ; \draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ] (71.94,130.23) .. controls (71.94,130.24) and (71.94,130.24) .. (71.94,130.24) .. controls (71.94,131.91) and (69.19,133.25) .. (65.79,133.25) .. controls (62.55,133.25) and (59.89,132.03) .. (59.65,130.47) ;  
	\draw  [draw opacity=0][fill={rgb, 255:red, 235; green, 235; blue, 210 }  ,fill opacity=1 ] (278.01,139.03) .. controls (278.01,139.03) and (278.01,139.03) .. (278.01,139.04) .. controls (278.01,140.7) and (275.26,142.05) .. (271.86,142.05) .. controls (268.62,142.05) and (265.96,140.82) .. (265.72,139.27) -- (271.86,139.04) -- cycle ; \draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ] (278.01,139.03) .. controls (278.01,139.03) and (278.01,139.03) .. (278.01,139.04) .. controls (278.01,140.7) and (275.26,142.05) .. (271.86,142.05) .. controls (268.62,142.05) and (265.96,140.82) .. (265.72,139.27) ;  
	\draw  [draw opacity=0][fill={rgb, 255:red, 235; green, 235; blue, 210 }  ,fill opacity=1 ] (297.37,130.23) .. controls (297.37,130.24) and (297.37,130.24) .. (297.37,130.24) .. controls (297.37,131.91) and (294.62,133.25) .. (291.22,133.25) .. controls (287.98,133.25) and (285.32,132.03) .. (285.08,130.47) -- (291.22,130.24) -- cycle ; \draw  [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ] (297.37,130.23) .. controls (297.37,130.24) and (297.37,130.24) .. (297.37,130.24) .. controls (297.37,131.91) and (294.62,133.25) .. (291.22,133.25) .. controls (287.98,133.25) and (285.32,132.03) .. (285.08,130.47) ;  
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][line width=1]    (489.54,121.97) -- (489.54,111.08) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][line width=1]    (559.08,121.77) -- (559.08,95.45) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][line width=1]    (512.55,121.97) -- (512.55,109.02) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][line width=1]    (535.03,121.77) -- (535.03,103.88) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][line width=1]    (581,121.56) -- (581,83.66) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][line width=1]    (600.34,121.56) -- (600.34,69.4) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][line width=1]    (421.81,121.56) -- (421.81,98.94) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][line width=1]    (444.82,122.18) -- (444.82,106.55) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][line width=1]    (466.27,121.77) -- (466.27,110.46) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][line width=1]    (400.71,121.56) -- (400.71,86.95) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][line width=1]    (381.68,122.04) -- (381.68,71.87) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][line width=1]    (618.01,121.56) -- (618.01,52.68) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][line width=1]    (362.62,120.95) -- (362.62,54.33) ;
	\draw [color={rgb, 255:red, 74; green, 74; blue, 74 }  ,draw opacity=1 ][line width=1]    (362.62,54.33) .. controls (463.18,164.29) and (589,88.62) .. (618.01,52.68) ;
	\draw [line width=1]    (339.05,122.21) -- (650.22,122.21) ;
	\draw [shift={(654.22,122.21)}, rotate = 180] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (13.4,-6.43) -- (0,0) -- (13.4,6.44) -- (8.9,0) -- cycle    ;
	\draw [line width=1]    (362.62,138.66) -- (362.62,33.93) ;
	\draw [shift={(362.62,29.93)}, rotate = 90] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (13.4,-6.43) -- (0,0) -- (13.4,6.44) -- (8.9,0) -- cycle    ;
	\draw (480.74,87.63) node [anchor=north west][inner sep=0.75pt]    {$%s$};
	\draw (346.95,45.9) node [anchor=north west][inner sep=0.75pt]    {$%s$};
	\draw (606.78,128) node [anchor=north west][inner sep=0.75pt]    {$%s$};
	\draw (345.85,22.38) node [anchor=north west][inner sep=0.75pt]    {$y$};
	\draw (639.2,96.4) node [anchor=north west][inner sep=0.75pt]    {$x$};
	\draw (342.33,125) node [anchor=north west][inner sep=0.75pt]    {$O$};
\end{tikzpicture}
\end{center} '''    'Biết dây dài nhất là $%s$ m, dây ngắn nhất là $%s$ m, khoảng cách giữa các dây bằng nhau, nhịp cầu dài $%s$ m. Biết mỗi sợi dây dài thêm $%s$phtram để neo cố định, tính chiều dài tổng cộng của các dây cáp dọc ở hai mặt bên.'
                                    %( latex(b),latex(a),latex(c),
                                    latex(a),latex(b),latex(c),latex(d)
                                    ))
                    
                    # Nội dung lời giải
                    loigiai = ('Gọi $y=ax^2+bx+c$ với $a \\ne 0$ là công thức của hàm số có đồ thị là thành cầu. \\\\ \n'
                            'Chọn hệ trục $(Oxy)$ như hình sau:'
                            r'''\begin{center}
	\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]    (230.11,228.65) -- (230.11,215.4) ;
		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]    (314.65,228.4) -- (314.65,196.4) ;
		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]    (258.08,228.65) -- (258.08,212.9) ;
		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]    (285.42,228.4) -- (285.42,206.65) ;
		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]    (342.31,228.15) -- (342.31,183.9) ;
		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]    (366.83,228.15) -- (366.83,167.4) ;
		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]    (147.76,228.15) -- (147.76,200.65) ;
		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]    (175.74,228.9) -- (175.74,209.9) ;
		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]    (201.82,228.4) -- (201.82,214.65) ;
		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]    (120.11,228.15) -- (120.11,187.4) ;
		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]    (94.96,228.15) -- (94.96,168.9) ;
		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]    (389.81,228.15) -- (389.81,146.4) ;
		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]    (72.79,227.4) -- (72.79,145.1) ;
		\draw [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=1 ][line width=1]    (72.8,146.4) .. controls (195.07,280.1) and (354.54,188.1) .. (389.81,144.4) ;
		\draw [line width=1]    (50.3,228.4) -- (426.8,228.4) ;
		\draw [shift={(430.8,228.4)}, rotate = 180] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (13.4,-6.43) -- (0,0) -- (13.4,6.44) -- (8.9,0) -- cycle    ;
		\draw [line width=1]    (72.3,249.4) -- (72.79,107.4) ;
		\draw [shift={(72.8,103.4)}, rotate = 90.2] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (13.4,-6.43) -- (0,0) -- (13.4,6.44) -- (8.9,0) -- cycle    ;
		\draw (53,233) node [anchor=north west][inner sep=0.75pt]    {$O$};
		\draw (414.3,211) node [anchor=north west][inner sep=0.75pt]    {$x$};
		\draw (52.8,102) node [anchor=north west][inner sep=0.75pt]    {$y$};
		\draw (379.3,233) node [anchor=north west][inner sep=0.75pt]    {$30$};
		\draw (53.3,129.4) node [anchor=north west][inner sep=0.75pt]    {$6$};
		\draw (222.3,196) node [anchor=north west][inner sep=0.75pt]    {$1$};
	\end{tikzpicture}
\end{center}''' 'Khi đó độ dài dây cáp dọc ở mỗi mặt bên là tung độ của điểm biểu diễn tương ứng. \\\\ \n'
                            'Ở mỗi mặt: có $13$ dây cáp dọc, tương ứng cho $12$ khoảng cách giữa chúng. \\\\ \n'
                            'Khoảng cách giữa hai dây cáp liền kề là $\\dfrac{%s}{12}=%s$. \\\\ \n'
                            'Từ vị trí các dây cáp ta thấy các điểm có tọa độ $(0;%s), (x_6;%s), (x_{12};%s)$ thuộc đồ thị hàm số. \\\\ \n'
                            'Trong đó $x_6=%s$ và $x_{12}=%s$. \\\\ \n'
                            'Suy ra ta có hệ phương trình \\\\ \n'
                            '\\hspace*{1cm} $\\heva{& 0a+0b+c=%s\\\\ & %s a+%s b+c=%s\\\\ & %s a+%s b+c=%s} \\Leftrightarrow \\heva{& a=%s\\\\ & b=%s \\\\ & c=%s.}$ \\\\ \n'
                            'Như vậy $y=%s$. \\\\ \n'
                            'Gọi $y_0, y_1, y_2, ..., y_{12}$ là tung độ của các điểm có hoành độ lần lượt là $x_0, x_1, x_2, ..., x_{12}$. \\\\ \n'
                            'Ta có \\\\ \n'
                            '\\hspace*{1cm} $y_0=%s; y_1=%s, y_{2}=%s; y_{3}=%s; y_{4}=%s; y_{5}=%s; y_{6}=%s;$ \\\\ \n'
                            '\\hspace*{1cm} $y_{7}=%s; y_{8}=%s; y_{9}=%s; y_{10}=%s; y_{11}=%s; y_{12}=%s$.\\\\ \n'
                            'Suy tổng chiều dài của các dây cáp dọc ở hai bên mặt chưa tính phần cáp neo dây là \\\\ \n'
                            '\\hspace*{1cm} $T_1=y_0+y_1+y_2+ \\cdots +y_{12}=%s$. \\\\ \n'
                            'Vậy tổng chiều dài của các dây cáp dọc ở hai bên mặt tính cả phần cáp neo dây là \\\\ \n'
                            '\\hspace*{1cm} $T=2 \\cdot %s \\left(1+\\dfrac{%s}{100} \\right)=%s \\approx %s$ m.'

                            %(latex(c),latex(a),latex(b),
                                latex(c),latex(c/12),
                                latex(a),latex(b),latex(a),
                                latex(Rational(c,2)),latex(c),
                                latex(a),
                                latex(Rational(c**2,4)),latex(Rational(c,2)),latex(b),
                                latex(c**2),latex(c),latex(a),
                                latex(hsa),latex(hsb),latex(hsc),
                                latex(f),
                                latex(f0),
                                latex(f1),latex(f2),latex(f3),latex(f4),latex(f5),latex(f6),latex(f7),latex(f8),latex(f9),latex(f10),latex(f11),latex(f12),
                                latex(kq1),
                                latex(kq1),latex(d),latex(kq),latex(kqz)
                            ))
                    
                    #Đáp án
                    dapan=' \\shortans[0]{$%s$} '%(latex(kqz))

                # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
                content = ('\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                    '\\loigiai{ \n'
                    +str(loigiai)+'}\n'
                    '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('phtram', '\\%')
                return content