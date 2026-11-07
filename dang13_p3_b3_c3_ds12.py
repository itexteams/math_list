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


def bt_dang13_p3_b3_c3_ds12(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        a=randint(5,20)
        while a%4!=0 or a==28:
            a=randint(5,20)
        h=a+10
        hs=nsimplify(-h/(a*a/4))
        s1=nsimplify(a*a*6*sqrt(3)/4)
        s2=nsimplify(2*a*h/3)
        s=nsimplify(s1+6*s2)      
        number = Decimal(float(s))  # Số cần làm tròn
        kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        
        # Nội dung câu hỏi
        noidungcauhoi = ('\\immini{'
                        'Để trang trí cho một phòng, người ta vẽ lên tường một hình như sau: trên mỗi cạnh của hình lục giác đều có cạnh bằng $%s$ cm có một cánh hoa '
                        'hình parabol, đỉnh của parabol cách cạnh $%s$ cm và nằm phía ngoài lục giác, đường parabol đó đi qua đầu mút của mỗi cạnh (như hình vẽ). Hỏi diện tích của hình vẽ trên tường bằng bao nhiêu cm$^2$? (kết quả làm tròn đến hàng đơn vị).'
                    '}{'
                    '''\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
	\\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (204.8,95) -- (185,129.29) -- (145.4,129.29) -- (125.6,95) -- (145.4,60.71) -- (185,60.71) -- cycle ;
	\\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (185.2,60.51) .. controls (171.98,7.01) and (158.78,7.01) .. (145.6,60.53) ;
	\\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (145.4,129.54) .. controls (158.92,182.96) and (172.12,182.88) .. (185,129.29) ;
	\\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (205.1,94.82) .. controls (244.5,56.28) and (237.8,44.91) .. (185,60.71) ;
	\\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (145.4,60.33) .. controls (92.67,44.31) and (85.92,55.65) .. (125.15,94.36) ;
	\\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (125.63,95.23) .. controls (85.86,133.37) and (92.45,144.81) .. (145.4,129.54) ;
	\\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (185.62,129.29) .. controls (238.69,144.13) and (245.19,132.64) .. (205.1,94.82) ;
\\end{tikzpicture} }'''
                
                %(latex(a),latex(h)))
        
        # Nội dung lời giải
        loigiai = ('Diện tích của hình lục giác đều là\\\\ \n'
                '\\hspace*{1cm} $S_1=6\\cdot%s^2\\cdot\\dfrac{\\sqrt{3}}{4}=%s$ cm$^2$.\\\\ \n'
                'Tính Diện tích của một hình parabol\\\\ \n'
                'Chọn hệ trục tọa độ như nhình vẽ\\\\ \n'
                '\\begin{center}\n'
                '\\begin{tikzpicture}[scale=1,>=stealth, font=\\footnotesize, line join=round, line cap=round]\n'
        '\\def\\a{-1} \\def\\b{0} \\def\\c{3}\n'
        '\\def\\xmin{-3} \\def\\xmax{3}\n'
        '\\def\\ymin{-0.1} \\def\\ymax{4}\n'
        '\\draw[->] (\\xmin,0)--(\\xmax,0) node [below]{$x$};\n'
        '\\draw[->] (0,\\ymin)--(0,\\ymax) node [left]{$y$};\n'
        '\\node at (0,0) [below left]{$O$};\n'
        '\\node at (2,0) [below]{$%s$};\n'
        '\\node at (-2,0) [below]{$%s$};\n'
        '\\node at (0,3) [above right]{$%s$};\n'
        '\\clip (\\xmin+0.1,\\ymin+0.1) rectangle (\\xmax-0.5,\\ymax-0.1);\n'
        '\\draw[smooth,samples=300] plot(\\x,{\\a*(\\x)^2+\\b*(\\x)+\\c});\n'
        '\\end{tikzpicture}\n'
        '\\end{center}\n'
        'Vì parabol cần tìm nhận trục $Oy$ làm trục đối xứng và cắt $Oy$ tại điểm có tung độ bằng $%s$ nên có dạng $y=ax^2+%s$.\\\\ \n'
        'Mặt khác parabol cắt $Ox$ tại điểm có tọa độ $\\left(%s;0\\right)$ nên ta có\\\\ \n'
        '\\hspace*{1cm} $a\\cdot\\left(%s\\right)^2+%s=0\\Rightarrow a=%s$.\\\\ \n'
        'Suy ra phương trình của parabol là $y=%sx^2+%s$.\\\\ \n'
        'Diện tích hình phẳng giới hạn bởi đường parabol $y=%sx^2+%s$, trục $Ox$ và hai đường thẳng $x=%s,x=%s$ là\\\\ \n'
        '\\hspace*{1cm} $S_2=\\displaystyle\\int\\limits_{%s}^{%s}\\left(%sx^2+%s\\right)\\text{d}x=%s$ cm$^2$.\\\\ \n'
        'Vậy diện tích của hình vẽ trên tường là\\\\ \n'
        '\\hspace*{1cm} $S=S_1+6\\cdot S_2=%s+6\\cdot%s\\approx %s$ cm$^2$.'
                
                %(latex(a),latex(s1),latex(nsimplify(a/2)),latex(nsimplify(-a/2)),latex(h),
                    latex(h),latex(h),latex(nsimplify(a/2)),latex(nsimplify(a/2)),latex(h),latex(hs),latex(hs),latex(h),
                    latex(hs),latex(h),latex(nsimplify(-a/2)),latex(nsimplify(a/2)),
                    latex(nsimplify(-a/2)),latex(nsimplify(a/2)),latex(hs),latex(h),latex(s2),
                    latex(s1),latex(s2),latex(kq)
                    )
                    )
        
        #Đáp án
        dapan=' \\shortans[0]{$%s$} '%(latex(kq))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
        '\\loigiai{ \n'
        +str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
    return content 