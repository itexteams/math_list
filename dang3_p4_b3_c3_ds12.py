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


def bt_dang3_p4_b3_c3_ds12(self):
                # Khai báo biến
                lisdang=['1']
                dang=random.choice(lisdang)
                if dang=='1':
                    a=randint(1,11)
                    
                    x = symbols('x')
                    f1 = pi*(sqrt(a**2-x**2))**2
                    
                    f2 = pi*(-sqrt(a**2-x**2)+2*a)**2
                    
                    v1=integrate(f1, (x, 0, a))
                    v2=integrate(f2, (x, -a, 0))
                    
                    h1=v1+v2  
                    number = Decimal(float(h1))  # Số cần làm tròn
                    kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                    
                    # Nội dung câu hỏi
                    noidungcauhoi = ('\\immini{'
                                    'Một vật trang trí có dạng một khối tròn xoay được tạo thành khi quay miền $(R)$ quanh trục $AB$. Miền $(R)$ được giới hạn bởi các cạnh $AB$, $AD$ của hình vuông $ABCD$ và các cung phần tư của các đường '
                                    'tròn bán kính bằng $%s$ cm với tâm lần lượt là trung điểm của các cạnh $AB$, $CD$. Tính thể tích của vật trang trí (làm tròn kết quả đến hàng đơn vị). \n'
                                    '}{'
                                    '''\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
	\\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (135,111.55) -- (280.46,111.55) -- (280.46,257) -- (135,257) -- cycle ;
	\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (280.46,111.54) .. controls (280.46,111.7) and (280.46,111.87) .. (280.46,112.04) .. controls (280.46,152.08) and (247.9,184.54) .. (207.73,184.54) .. controls (167.56,184.54) and (135,152.08) .. (135,112.04) .. controls (135,111.88) and (135,111.71) .. (135,111.55) -- cycle ;
	\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (207.73,117.17) -- (280.19,117.17) -- (280.19,256.6) -- (207.73,256.6) -- cycle ;
	\\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (135,257) .. controls (135,256.89) and (135,256.77) .. (135,256.66) .. controls (134.7,216.62) and (167.17,183.92) .. (207.51,183.63) .. controls (247.85,183.33) and (280.79,215.55) .. (281.08,255.59) .. controls (281.08,255.9) and (281.08,256.22) .. (281.08,256.53) -- cycle ;
	\\draw  [draw opacity=0] (200.03,184.09) .. controls (202.82,183.77) and (205.66,183.6) .. (208.54,183.6) .. controls (248.6,183.6) and (281.08,215.84) .. (281.08,255.6) .. controls (281.08,255.92) and (281.08,256.23) .. (281.08,256.55) -- (208.54,255.6) -- cycle ; \\draw   (200.03,184.09) .. controls (202.82,183.77) and (205.66,183.6) .. (208.54,183.6) .. controls (248.6,183.6) and (281.08,215.84) .. (281.08,255.6) .. controls (281.08,255.92) and (281.08,256.23) .. (281.08,256.55) ;  
	\\draw (116,250.91) node [anchor=north west][inner sep=0.75pt]    {$A$};
	\\draw (284,249.58) node [anchor=north west][inner sep=0.75pt]    {$B$};
	\\draw (284,99.58) node [anchor=north west][inner sep=0.75pt]    {$C$};
	\\draw (115.33,94.58) node [anchor=north west][inner sep=0.75pt]    {$D$};
\\end{tikzpicture} }'''
                                    %(latex(a)
                                    ))
                    
                    # Nội dung lời giải
                    loigiai = ('''\\begin{center}
	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
		\\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (135,111.55) -- (280.46,111.55) -- (280.46,257) -- (135,257) -- cycle ;
		\\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (280.46,111.54) .. controls (280.46,111.7) and (280.46,111.87) .. (280.46,112.04) .. controls (280.46,152.08) and (247.9,184.54) .. (207.73,184.54) .. controls (167.56,184.54) and (135,152.08) .. (135,112.04) .. controls (135,111.88) and (135,111.71) .. (135,111.55) -- cycle ;
		\\draw  [draw opacity=0][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (207.73,117.17) -- (280.19,117.17) -- (280.19,256.6) -- (207.73,256.6) -- cycle ;
		\\draw  [draw opacity=0][fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (135,257) .. controls (135,256.89) and (135,256.77) .. (135,256.66) .. controls (134.7,216.62) and (167.17,183.92) .. (207.51,183.63) .. controls (247.85,183.33) and (280.79,215.55) .. (281.08,255.59) .. controls (281.08,255.9) and (281.08,256.22) .. (281.08,256.53) -- cycle ;
		\\draw  [draw opacity=0] (200.03,184.09) .. controls (202.82,183.77) and (205.66,183.6) .. (208.54,183.6) .. controls (248.6,183.6) and (281.08,215.84) .. (281.08,255.6) .. controls (281.08,255.92) and (281.08,256.23) .. (281.08,256.55) -- (208.54,255.6) -- cycle ; \\draw   (200.03,184.09) .. controls (202.82,183.77) and (205.66,183.6) .. (208.54,183.6) .. controls (248.6,183.6) and (281.08,215.84) .. (281.08,255.6) .. controls (281.08,255.92) and (281.08,256.23) .. (281.08,256.55) ;  
		\\draw    (105.79,257.65) -- (313.81,256.86) ;
		\\draw [shift={(315.81,256.85)}, rotate = 179.78] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
		\\draw    (206.01,279.65) -- (206.01,78.45) ;
		\\draw [shift={(206.01,76.45)}, rotate = 90] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
		\\draw (113.2,258.11) node [anchor=north west][inner sep=0.75pt]    {$A$};
		\\draw (272,258.58) node [anchor=north west][inner sep=0.75pt]    {$B$};
		\\draw (284,99.58) node [anchor=north west][inner sep=0.75pt]    {$C$};
		\\draw (115.33,94.58) node [anchor=north west][inner sep=0.75pt]    {$D$};
		\\draw (185.91,258.91) node [anchor=north west][inner sep=0.75pt]    {$O$};
		\\draw (297.91,229.91) node [anchor=north west][inner sep=0.75pt]    {$x$};
		\\draw (188.58,72.24) node [anchor=north west][inner sep=0.75pt]    {$y$};
		\\draw (188.58,113.24) node [anchor=north west][inner sep=0.75pt]    {$F$};
		\\draw (188.58,160.91) node [anchor=north west][inner sep=0.75pt]    {$E$};
	\\end{tikzpicture}	
\\end{center}''' 'Gắn hệ trục tọa độ $(Oxy)$ sao cho $O(0;0)$ là trung điểm đoạn thẳng $AB$. \\\\ \n'
                            'Với hai điểm $E\\left(0; %s \\right)$ và $F(0; %s)$. \\\\ \n'            
                            'Khi đó \\\\ \n'
                            '\\hspace*{1cm} Đường tròn tâm $O$ chứa cung tròn $BE$ có phương trình $x^2 + y^2 = %s$. \\\\ \n'
                            '\\hspace*{1cm} Đường tròn tâm $F$ chứa cung tròn $DE$ có phương trình $x^2 + (y-%s)^2 = %s$. \\\\ \n'           
                            'Suy ra \\\\ \n'
                            '\\hspace*{1cm} Phương trình cung trên của đường tròn tâm $O$ là $y = \\sqrt{%s-x^2}$. \\\\ \n'
                            '\\hspace*{1cm} Phương trình cung dưới của đường tròn tâm $F$ là $y = -\\sqrt{%s-x^2} + %s$. \\\\ \n'            
                            'Khi đó, thể tích vật thể trang trí là \\\\ \n'            
                            '\\hspace*{1cm} $V = \\pi \\int\\limits_0^%s \\left(\\sqrt{%s-x^2}\\right)^2 \\text{d}x + \\pi \\int\\limits_{-%s}^0 \\left(-\\sqrt{%s-x^2} + %s\\right)^2 \\text{d}x \\approx %s$ cm$^3$.'
                            %(latex(a),latex(2*a),latex(a**2),latex(2*a),latex(a**2),
                                latex(a**2),latex(a**2),latex(2*a),
                                latex(a),latex(a**2),latex(a),latex(a**2),latex(2*a),latex(kq)
                                
                            ))
                    
                    #Đáp án
                  

                # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
                content = ('\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n'+ str(noidungcauhoi)+
                    '\\loigiai{ \n'
                    +str(loigiai)+'}\n'
                    '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
                return content 