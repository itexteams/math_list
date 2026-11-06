import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

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


def bt_dang1_p4_b4_c1_ds12(self):
            # Khai báo biến
            lisdang=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36']
            dang=random.choice(lisdang)
            if dang=='36':
                kq=4
                # Câu hỏi
                noidungcauhoi = ('\\immini{ '
                                'Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có đồ thị như hình vẽ. Trong các giá trị $a, b, c, d$ tìm các giá trị dương.'
                                '}{'                    
                                '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-5.1,0)--(2.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,-3.1)--(0,3.1) node[below left] {$y$}; \n'
                                '\\draw (0,0) node [below right] {$O$}; \n'
                                '\\draw[dashed,thin](-3,0)--(-3,2)--(0,2); \n'
                                '\\draw[dashed,thin](-1,0)--(-1,-2)--(0,-2); \n'
                                '\\begin{scope} \n'
                                '\\clip (-5,-3) rectangle (2,3); \n'
                                '\\draw[samples=200,domain=-5:2,smooth,variable=\\x] plot (\\x,{1*((\\x)^3)+6*((\\x)^2)+9*(\\x)+2});  \n'
                                '\\end{scope} \n'
                                '\\end{tikzpicture}} \n'

                                '}')


                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy \\\\ \n'
                        '\\hspace*{1cm} Nhánh ngoài cùng bên phải, từ trái sang phải đi lên nên $a>0$. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị cắt trục $Oy$ tại điểm nằm phía trên gốc tọa độ nên $d>0$. \\\\ \n'
                        'Gọi $x_1, x_2$ là hai điểm cực trị của hàm số, với $x_1 < x_2$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1 < x_2 <0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2<0 \\Rightarrow -\\dfrac{b}{a} <0 \\Leftrightarrow \\dfrac{b}{a} >0$. Vì $a>0$ nên $b>0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 >0 \\Rightarrow \\dfrac{c}{a} >0$. Vì $a>0$ nên $c>0$. \\\\ \n'
                        'Vậy $a>0, b>0, c>0, d>0$.'
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='35':
                kq=3
                # Câu hỏi
                noidungcauhoi = ('\\immini{ '
                                'Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có đồ thị như hình vẽ. Trong các giá trị $a, b, c, d$ tìm các giá trị dương.'
                                '}{'                    
                                '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-5.1,0)--(2.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,-5.1)--(0,2.1) node[below left] {$y$}; \n'
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw[dashed,thin](-1,0)--(-1,-4)--(0,-4); \n'
                                '\\begin{scope} \n'
                                '\\clip (-5,-5) rectangle (2,2); \n'
                                '\\draw[samples=200,domain=-5:2,smooth,variable=\\x] plot (\\x,{1*((\\x)^3)+6*((\\x)^2)+9*(\\x)+0});  \n'
                                '\\end{scope} \n'
                                '\\end{tikzpicture}} \n'

                                '}')


                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy \\\\ \n'
                        '\\hspace*{1cm} Nhánh ngoài cùng bên phải, từ trái sang phải đi lên nên $a>0$. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị cắt trục $Oy$ tại gốc tọa độ nên $d=0$. \\\\ \n'
                        'Gọi $x_1, x_2$ là hai điểm cực trị của hàm số, với $x_1 < x_2$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1 < x_2 <0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2<0 \\Rightarrow -\\dfrac{b}{a} <0 \\Leftrightarrow \\dfrac{b}{a} >0$. Vì $a>0$ nên $b>0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 >0 \\Rightarrow \\dfrac{c}{a} >0$. Vì $a>0$ nên $c>0$. \\\\ \n'
                        'Vậy $a>0, b>0, c>0, d=0$.'
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='34':
                kq=3
                # Câu hỏi
                noidungcauhoi = ('\\immini{ '
                                'Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có đồ thị như hình vẽ. Trong các giá trị $a, b, c, d$ tìm các giá trị dương.'
                                '}{'                    
                                '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-5.1,0)--(2.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,-6.1)--(0,1.1) node[below left] {$y$}; \n'
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw[dashed,thin](-3,0)--(-3,-1)--(0,-1); \n'
                                '\\draw[dashed,thin](-1,0)--(-1,-5)--(0,-5); \n'
                                '\\begin{scope} \n'
                                '\\clip (-5,-6) rectangle (2,1); \n'
                                '\\draw[samples=200,domain=-5:2,smooth,variable=\\x] plot (\\x,{1*((\\x)^3)+6*((\\x)^2)+9*(\\x)+-1});  \n'
                                '\\end{scope} \n'
                                '\\end{tikzpicture} }\n'

                                '}')


                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy \\\\ \n'
                        '\\hspace*{1cm} Nhánh ngoài cùng bên phải, từ trái sang phải đi lên nên $a>0$. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị cắt trục $Oy$ tại điểm nằm phía dưới gốc tọa độ nên $d<0$. \\\\ \n'
                        'Gọi $x_1, x_2$ là hai điểm cực trị của hàm số, với $x_1 < x_2$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1 < x_2 <0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2<0 \\Rightarrow -\\dfrac{b}{a} <0 \\Leftrightarrow \\dfrac{b}{a} >0$. Vì $a>0$ nên $b>0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 >0 \\Rightarrow \\dfrac{c}{a} >0$. Vì $a>0$ nên $c>0$. \\\\ \n'
                        'Vậy $a>0, b>0, c>0, d<0$.'
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='33':
                kq=3
                # Câu hỏi
                noidungcauhoi = ('\\immini{ '
                                'Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có đồ thị như hình vẽ. Trong các giá trị $a, b, c, d$ tìm các giá trị dương.'
                                '}{'                    
                                '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-4.1,0)--(2.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,-1.1)--(0,6.1) node[below left] {$y$}; \n'
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw[dashed,thin](-2,0)--(-2,5)--(0,5); \n'
                                '\\begin{scope} \n'
                                '\\clip (-4,-1) rectangle (2,6); \n'
                                '\\draw[samples=200,domain=-4:2,smooth,variable=\\x] plot (\\x,{1*((\\x)^3)+3*((\\x)^2)+0*(\\x)+1}); \n'
                                '\\end{scope} \n'
                                '\\end{tikzpicture} } \n'

                                '}')


                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy \\\\ \n'
                        '\\hspace*{1cm} Nhánh ngoài cùng bên phải, từ trái sang phải đi lên nên $a>0$. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị cắt trục $Oy$ tại điểm nằm phía trên gốc tọa độ nên $d>0$. \\\\ \n'
                        'Gọi $x_1, x_2$ là hai điểm cực trị của hàm số, với $x_1 < x_2$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1 < x_2 = 0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2<0 \\Rightarrow -\\dfrac{b}{a} <0 \\Leftrightarrow \\dfrac{b}{a} >0$. Vì $a>0$ nên $b>0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 =0 \\Rightarrow \\dfrac{c}{a} =0$. Vì $a \\ne 0$ nên $c=0$. \\\\ \n'
                        'Vậy $a>0, b>0, c=0, d>0$.'
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='32':
                kq=2
                # Câu hỏi
                noidungcauhoi = ('\\immini{ '
                                'Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có đồ thị như hình vẽ. Trong các giá trị $a, b, c, d$ tìm các giá trị dương.'
                                '}{'                    
                                '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-4.1,0)--(2.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,-1.1)--(0,5.1) node[below left] {$y$}; \n'
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw[dashed,thin](-2,0)--(-2,4)--(0,4); \n'
                                '\\begin{scope} \n'
                                '\\clip (-4,-1) rectangle (2,5); \n'
                                '\\draw[samples=200,domain=-4:2,smooth,variable=\\x] plot (\\x,{1*((\\x)^3)+3*((\\x)^2)+0*(\\x)+0});  \n'
                                '\\end{scope} \n'
                                '\\end{tikzpicture}} \n'

                                '}')


                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy \\\\ \n'
                        '\\hspace*{1cm} Nhánh ngoài cùng bên phải, từ trái sang phải đi lên nên $a>0$. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị cắt trục $Oy$ tại gốc tọa độ nên $d=0$. \\\\ \n'
                        'Gọi $x_1, x_2$ là hai điểm cực trị của hàm số, với $x_1 < x_2$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1 < x_2 = 0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2<0 \\Rightarrow -\\dfrac{b}{a} <0 \\Leftrightarrow \\dfrac{b}{a} >0$. Vì $a>0$ nên $b>0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 =0 \\Rightarrow \\dfrac{c}{a} =0$. Vì $a \\ne 0$ nên $c=0$. \\\\ \n'
                        'Vậy $a>0, b>0, c=0, d=0$.'
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='31':
                kq=2
                # Câu hỏi
                noidungcauhoi = ('\\immini{ '
                                'Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có đồ thị như hình vẽ. Trong các giá trị $a, b, c, d$ tìm các giá trị dương.'
                                '}{'                    
                                '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-4.1,0)--(2.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,-2.1)--(0,4.1) node[below left] {$y$}; \n'
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw[dashed,thin](-2,0)--(-2,3)--(0,3); \n'
                                '\\begin{scope} \n'
                                '\\clip (-4,-2) rectangle (2,4); \n'
                                '\\draw[samples=200,domain=-4:2,smooth,variable=\\x] plot (\\x,{1*((\\x)^3)+3*((\\x)^2)+0*(\\x)+-1});  \n'
                                '\\end{scope} \n'
                                '\\end{tikzpicture}} \n'

                                '}')


                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy \\\\ \n'
                        '\\hspace*{1cm} Nhánh ngoài cùng bên phải, từ trái sang phải đi lên nên $a>0$. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị cắt trục $Oy$ tại điểm nằm phía dưới gốc tọa độ nên $d<0$. \\\\ \n'
                        'Gọi $x_1, x_2$ là hai điểm cực trị của hàm số, với $x_1 < x_2$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1 < x_2 = 0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2<0 \\Rightarrow -\\dfrac{b}{a} <0 \\Leftrightarrow \\dfrac{b}{a} >0$. Vì $a>0$ nên $b>0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 =0 \\Rightarrow \\dfrac{c}{a} =0$. Vì $a \\ne 0$ nên $c=0$. \\\\ \n'
                        'Vậy $a>0, b>0, c=0, d<0$.'
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='30':
                kq=1
                # Câu hỏi
                noidungcauhoi = ('\\immini{ '
                                'Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có đồ thị như hình vẽ. Trong các giá trị $a, b, c, d$ tìm các giá trị dương.'
                                '}{'                    
                                '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-3.1,0)--(2.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,-1.1)--(0,6.1) node[below left] {$y$}; \n'
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw[dashed,thin](-1.5,0)--(-1.5,4.6)--(0,4.6); \n'
                                '\\draw[dashed,thin](0.5,0)--(0.5,0.6)--(0,0.6); \n'
                                '\\begin{scope} \n'
                                '\\clip (-3,-2) rectangle (2,6); \n'
                                '\\draw[samples=200,domain=-2.65:2,smooth,variable=\\x] plot (\\x,{1*((\\x)^3)+1.5*((\\x)^2)+-2.25*(\\x)+1.25});  \n'
                                '\\end{scope} \n'
                                '\\end{tikzpicture} }\n'

                                '}')


                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy \\\\ \n'
                        '\\hspace*{1cm} Nhánh ngoài cùng bên phải, từ trái sang phải đi lên nên $a>0$. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị cắt trục $Oy$ tại điểm nằm phía trên gốc tọa độ nên $d>0$. \\\\ \n'
                        'Gọi $x_1, x_2$ là hai điểm cực trị của hàm số, với $x_1 < x_2$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1 <0< x_2$ và $\\abs{x_1} > \\abs{x_2}$. \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2<0 \\Rightarrow -\\dfrac{b}{a} <0 \\Leftrightarrow \\dfrac{b}{a} >0$. Vì $a>0$ nên $b>0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 <0 \\Rightarrow \\dfrac{c}{a} <0$. Vì $a>0$ nên $c<0$. \\\\ \n'
                        'Vậy $a>0, b>0, c<0, d>0$.'
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='29':
                kq=1
                # Câu hỏi
                noidungcauhoi = ('\\immini{ '
                                'Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có đồ thị như hình vẽ. Trong các giá trị $a, b, c, d$ tìm các giá trị dương.'
                                '}{'                    
                                '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-3.1,0)--(2.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,-1.1)--(0,4.1) node[below left] {$y$}; \n'
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw[dashed,thin](-1.5,0)--(-1.5,3.4)--(0,3.4); \n'
                                '\\draw[dashed,thin](0.5,0)--(0.5,-0.6)--(0,-0.6);  \n'
                                '\\begin{scope} \n'
                                '\\clip (-3,-2) rectangle (2,4); \n'
                                '\\draw[samples=200,domain=-2.5:1.55,smooth,variable=\\x] plot (\\x,{1*((\\x)^3)+1.5*((\\x)^2)+-2.25*(\\x)+0});  \n'
                                '\\end{scope} \n'
                                '\\end{tikzpicture}} \n'

                                '}')


                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy \\\\ \n'
                        '\\hspace*{1cm} Nhánh ngoài cùng bên phải, từ trái sang phải đi lên nên $a>0$. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị cắt trục $Oy$ tại gốc tọa độ nên $d=0$. \\\\ \n'
                        'Gọi $x_1, x_2$ là hai điểm cực trị của hàm số, với $x_1 < x_2$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1 <0< x_2$ và $\\abs{x_1} > \\abs{x_2}$. \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2<0 \\Rightarrow -\\dfrac{b}{a} <0 \\Leftrightarrow \\dfrac{b}{a} >0$. Vì $a>0$ nên $b>0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 <0 \\Rightarrow \\dfrac{c}{a} <0$. Vì $a>0$ nên $c<0$. \\\\ \n'
                        'Vậy $a>0, b>0, c<0, d=0$.'
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='28':
                kq=2
                # Câu hỏi
                noidungcauhoi = ('\\immini{ '
                                'Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có đồ thị như hình vẽ. Trong các giá trị $a, b, c, d$ tìm các giá trị dương.'
                                '}{'                    
                                '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-3.1,0)--(2.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,-2.1)--(0,3.1) node[below left] {$y$}; \n'
                                '\\draw (0,0) node [below right] {$O$}; \n'
                                '\\draw[dashed,thin](-1.5,0)--(-1.5,2.4)--(0,2.4); \n'
                                '\\draw[dashed,thin](0.5,0)--(0.5,-1.6)--(0,-1.6); \n'
                                '\\begin{scope} \n'
                                '\\clip (-3,-2) rectangle (2,3); \n'
                                '\\draw[samples=200,domain=-2.6:1.55,smooth,variable=\\x] plot (\\x,{1*((\\x)^3)+1.5*((\\x)^2)+-2.25*(\\x)-1});  \n'
                                '\\end{scope} \n'
                                '\\end{tikzpicture} } \n'

                                '}')


                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy \\\\ \n'
                        '\\hspace*{1cm} Nhánh ngoài cùng bên phải, từ trái sang phải đi lên nên $a>0$. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị cắt trục $Oy$ tại điểm nằm phía dưới gốc tọa độ nên $d<0$. \\\\ \n'
                        'Gọi $x_1, x_2$ là hai điểm cực trị của hàm số, với $x_1 < x_2$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1 <0< x_2$ và $\\abs{x_1} > \\abs{x_2}$. \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2<0 \\Rightarrow -\\dfrac{b}{a} <0 \\Leftrightarrow \\dfrac{b}{a} >0$. Vì $a>0$ nên $b>0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 <0 \\Rightarrow \\dfrac{c}{a} <0$. Vì $a>0$ nên $c<0$. \\\\ \n'
                        'Vậy $a>0, b>0, c<0, d<0$.'
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='27':
                kq=2
                # Câu hỏi
                noidungcauhoi = ('\\immini{ '
                                'Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có đồ thị như hình vẽ. Trong các giá trị $a, b, c, d$ tìm các giá trị dương.'
                                '}{'                    
                                '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-3.1,0)--(3.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,-1.1)--(0,6.1) node[below left] {$y$}; \n'
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw[dashed,thin](-0.5,0)--(-0.5,5)--(0,5); \n'
                                '\\draw[dashed,thin](1.5,0)--(1.5,1)--(0,1); \n'
                                '\\begin{scope} \n'
                                '\\clip (-3,-1) rectangle (3,6); \n'
                                '\\draw[samples=200,domain=-3:3,smooth,variable=\\x] plot (\\x,{1*((\\x)^3)+-1.5*((\\x)^2)+-2.25*(\\x)+4.35});  \n'
                                '\\end{scope} \n'
                                '\\end{tikzpicture}} \n'

                                '}')


                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy \\\\ \n'
                        '\\hspace*{1cm} Nhánh ngoài cùng bên phải, từ trái sang phải đi lên nên $a>0$. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị cắt trục $Oy$ tại điểm nằm phía trên gốc tọa độ nên $d>0$. \\\\ \n'
                        'Gọi $x_1, x_2$ là hai điểm cực trị của hàm số, với $x_1 < x_2$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1 <0< x_2$ và $\\abs{x_1}<\\abs{x_2}$. \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2>0 \\Rightarrow -\\dfrac{b}{a} >0 \\Leftrightarrow \\dfrac{b}{a} <0$. Vì $a>0$ nên $b<0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 <0 \\Rightarrow \\dfrac{c}{a} <0$. Vì $a>0$ nên $c<0$. \\\\ \n'
                        'Vậy $a>0, b<0, c<0, d>0$.'
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='26':
                kq=2
                # Câu hỏi
                noidungcauhoi = ('\\immini{ '
                                'Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có đồ thị như hình vẽ. Trong các giá trị $a, b, c, d$ tìm các giá trị âm.'
                                '}{'                    
                                '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]  \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-2.1,0)--(3.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,-4.1)--(0,2.1) node[below left] {$y$}; \n'
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw[dashed,thin](-0.5,0)--(-0.5,0.6)--(0,0.6); \n'
                                '\\draw[dashed,thin](1.5,0)--(1.5,-3.4)--(0,-3.4); \n'
                                '\\begin{scope} \n'
                                '\\clip (-2,-4) rectangle (3,2); \n'
                                '\\draw[samples=200,domain=-2:3,smooth,variable=\\x] plot (\\x,{1*((\\x)^3)+-1.5*((\\x)^2)+-2.25*(\\x)+0});  \n'
                                '\\end{scope} \n'
                                '\\end{tikzpicture} }\n'

                                '}')


                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy \\\\ \n'
                        '\\hspace*{1cm} Nhánh ngoài cùng bên phải, từ trái sang phải đi lên nên $a>0$. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị cắt trục $Oy$ tại gốc tọa độ nên $d=0$. \\\\ \n'
                        'Gọi $x_1, x_2$ là hai điểm cực trị của hàm số, với $x_1 < x_2$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1 <0< x_2$ và $\\abs{x_1}<\\abs{x_2}$. \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2>0 \\Rightarrow -\\dfrac{b}{a} >0 \\Leftrightarrow \\dfrac{b}{a} <0$. Vì $a>0$ nên $b<0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 <0 \\Rightarrow \\dfrac{c}{a} <0$. Vì $a>0$ nên $c<0$. \\\\ \n'
                        'Vậy $a>0, b<0, c<0, d=0$.'
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='25':
                kq=3
                # Câu hỏi
                noidungcauhoi = ('\\immini{ '
                                'Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có đồ thị như hình vẽ. Trong các giá trị $a, b, c, d$ tìm các giá trị âm.'
                                '}{'                    
                                '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-2.1,0)--(3.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,-5.1)--(0,1.1) node[below left] {$y$}; \n'
                                '\\draw (0,0) node [below right] {$O$}; \n'
                                '\\draw[dashed,thin](-0.5,0)--(-0.5,-0.4)--(0,-0.4); \n'
                                '\\draw[dashed,thin](1.5,0)--(1.5,-4.4)--(0,-4.4); \n'
                                '\\begin{scope} \n'
                                '\\clip (-2,-5) rectangle (3,1); \n'
                                '\\draw[samples=200,domain=-2:3,smooth,variable=\\x] plot (\\x,{1*((\\x)^3)+-1.5*((\\x)^2)+-2.25*(\\x)+-1}); \n'
                                '\\end{scope} \n'
                                '\\end{tikzpicture}} \n'

                                '}')


                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy \\\\ \n'
                        '\\hspace*{1cm} Nhánh ngoài cùng bên phải, từ trái sang phải đi lên nên $a>0$. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị cắt trục $Oy$ tại điểm nằm phía trên gốc tọa độ nên $d<0$. \\\\ \n'
                        'Gọi $x_1, x_2$ là hai điểm cực trị của hàm số, với $x_1 < x_2$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1 <0< x_2$ và $\\abs{x_1}<\\abs{x_2}$. \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2>0 \\Rightarrow -\\dfrac{b}{a} >0 \\Leftrightarrow \\dfrac{b}{a} <0$. Vì $a>0$ nên $b<0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 <0 \\Rightarrow \\dfrac{c}{a} <0$. Vì $a>0$ nên $c<0$. \\\\ \n'
                        'Vậy $a>0, b<0, c<0, d<0$.'
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='24':
                kq=2
                # Câu hỏi
                noidungcauhoi = ('\\immini{ '
                                'Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có đồ thị như hình vẽ. Trong các giá trị $a, b, c, d$ tìm các giá trị dương.'
                                '}{'                    
                                '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-2.1,0)--(4.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,-1.1)--(0,6.1) node[below left] {$y$}; \n'
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw[dashed,thin](2,0)--(2,1)--(0,1); \n'
                                '\\begin{scope} \n'
                                '\\clip (-2,-1) rectangle (4,6); \n'
                                '\\draw[samples=200,domain=-2:4,smooth,variable=\\x] plot (\\x,{1*((\\x)^3)+-3*((\\x)^2)+0*(\\x)+5});  \n'
                                '\\end{scope} \n'
                                '\\end{tikzpicture} }\n'

                                '}')


                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy \\\\ \n'
                        '\\hspace*{1cm} Nhánh ngoài cùng bên phải, từ trái sang phải đi lên nên $a>0$. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị cắt trục $Oy$ tại điểm nằm phía trên gốc tọa độ nên $d>0$. \\\\ \n'
                        'Gọi $x_1, x_2$ là hai điểm cực trị của hàm số, với $x_1 < x_2$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1 =0 < x_2$. \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2>0 \\Rightarrow -\\dfrac{b}{a} >0 \\Leftrightarrow \\dfrac{b}{a} <0$. Vì $a>0$ nên $b<0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 =0 \\Rightarrow \\dfrac{c}{a} =0$. Vì $a>0$ nên $c=0$. \\\\ \n'
                        'Vậy $a>0, b<0, c=0, d>0$.'
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='23':
                kq=1
                # Câu hỏi
                noidungcauhoi = ('\\immini{ '
                                'Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có đồ thị như hình vẽ. Trong các giá trị $a, b, c, d$ tìm các giá trị dương.'
                                '}{'                    
                                '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-2.1,0)--(4.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,-5.1)--(0,1.1) node[below left] {$y$}; \n'
                                '\\draw (0,0) node [above left] {$O$}; \n'
                                '\\draw[dashed,thin](2,0)--(2,-4)--(0,-4); \n'
                                '\\begin{scope} \n'
                                '\\clip (-2,-5) rectangle (4,1); \n'
                                '\\draw[samples=200,domain=-2:4,smooth,variable=\\x] plot (\\x,{1*((\\x)^3)+-3*((\\x)^2)+0*(\\x)+0});  \n'
                                '\\end{scope} \n'
                                '\\end{tikzpicture} } \n'

                                '}')


                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy \\\\ \n'
                        '\\hspace*{1cm} Nhánh ngoài cùng bên phải, từ trái sang phải đi lên nên $a>0$. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị cắt trục $Oy$ tại gốc tọa độ nên $d=0$. \\\\ \n'
                        'Gọi $x_1, x_2$ là hai điểm cực trị của hàm số, với $x_1 < x_2$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1 =0 < x_2$. \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2>0 \\Rightarrow -\\dfrac{b}{a} >0 \\Leftrightarrow \\dfrac{b}{a} <0$. Vì $a>0$ nên $b<0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 =0 \\Rightarrow \\dfrac{c}{a} =0$. Vì $a>0$ nên $c=0$. \\\\ \n'
                        'Vậy $a>0, b<0, c=0, d=0$.'
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='22':
                kq=1
                # Câu hỏi
                noidungcauhoi = ('\\immini{ '
                                'Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có đồ thị như hình vẽ. Trong các giá trị $a, b, c, d$ tìm các giá trị dương.'
                                '}{'                    
                                '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-2.1,0)--(4.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,-6.1)--(0,1.1) node[below left] {$y$}; \n'
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw[dashed,thin](2,0)--(2,-5)--(0,-5); \n'
                                '\\begin{scope} \n'
                                '\\clip (-2,-6) rectangle (4,1); \n'
                                '\\draw[samples=200,domain=-2:4,smooth,variable=\\x] plot (\\x,{1*((\\x)^3)+-3*((\\x)^2)+0*(\\x)+-1});  \n'
                                '\\end{scope} \n'
                                '\\end{tikzpicture} } \n'

                                '}')


                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy \\\\ \n'
                        '\\hspace*{1cm} Nhánh ngoài cùng bên phải, từ trái sang phải đi lên nên $a>0$. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị cắt trục $Oy$ tại điểm nằm phía dưới gốc tọa độ nên $d<0$. \\\\ \n'
                        'Gọi $x_1, x_2$ là hai điểm cực trị của hàm số, với $x_1 < x_2$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1 =0 < x_2$. \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2>0 \\Rightarrow -\\dfrac{b}{a} >0 \\Leftrightarrow \\dfrac{b}{a} <0$. Vì $a>0$ nên $b<0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 =0 \\Rightarrow \\dfrac{c}{a} =0$. Vì $a>0$ nên $c=0$. \\\\ \n'
                        'Vậy $a>0, b<0, c=0, d<0$.'
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='21':
                kq=3
                # Câu hỏi
                noidungcauhoi = ('\\immini{ '
                                'Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có đồ thị như hình vẽ. Trong các giá trị $a, b, c, d$ tìm các giá trị dương.'
                                '}{'                    
                                '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                            '\\tikzset{every node/.style={scale=0.9}} \n'
                            '\\draw[->] (-1.1,0)--(5.1,0) node[below left] {$x$}; \n'
                            '\\draw[->] (0,-1.1)--(0,6.1) node[below left] {$y$}; \n'
                            '\\draw (0,0) node [below right] {$O$}; \n'
                            '\\draw[dashed,thin](1,0)--(1,5)--(0,5); \n'
                            '\\draw[dashed,thin](3,0)--(3,1)--(0,1); \n'
                            '\\begin{scope} \n'
                            '\\clip (-1,-1) rectangle (5,6); \n'
                            '\\draw[samples=200,domain=-1:5,smooth,variable=\\x] plot (\\x,{1*((\\x)^3)+-6*((\\x)^2)+9*(\\x)+1});  \n'
                            '\\end{scope} \n'
                            '\\end{tikzpicture} }\n'

                                '}')


                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy \\\\ \n'
                        '\\hspace*{1cm} Nhánh ngoài cùng bên phải, từ trái sang phải đi lên nên $a>0$. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị cắt trục $Oy$ tại điểm nằm phía trên gốc tọa độ nên $d>0$. \\\\ \n'
                        'Gọi $x_1, x_2$ là hai điểm cực trị của hàm số, với $x_1 < x_2$, ta có \\\\ \n'
                        '\\hspace*{1cm} $0< x_1 < x_2$. \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2>0 \\Rightarrow -\\dfrac{b}{a} >0 \\Leftrightarrow \\dfrac{b}{a} <0$. Vì $a>0$ nên $b<0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 >0 \\Rightarrow \\dfrac{c}{a} >0$. Vì $a>0$ nên $c>0$. \\\\ \n'
                        'Vậy $a>0, b<0, c>0, d>0$.'
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='20':
                kq=1
                # Câu hỏi
                noidungcauhoi = ('\\immini{ '
                                'Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có đồ thị như hình vẽ. Trong các giá trị $a, b, c, d$ tìm các giá trị âm.'
                                '}{'                    
                                '\\scalebox{0.6}{ \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                            '\\tikzset{every node/.style={scale=0.9}} \n'
                            '\\draw[->] (-1.1,0)--(5.1,0) node[below left] {$x$}; \n'
                            '\\draw[->] (0,-1.1)--(0,5.1) node[below left] {$y$}; \n'
                            '\\draw (0,0) node [below left] {$O$}; \n'
                            '\\draw[dashed,thin](1,0)--(1,4)--(0,4); \n'
                            '\\begin{scope} \n'
                            '\\clip (-1,-1) rectangle (5,5); \n'
                            '\\draw[samples=200,domain=-1:5,smooth,variable=\\x] plot (\\x,{1*((\\x)^3)+-6*((\\x)^2)+9*(\\x)+0}); \n'
                            '\\end{scope} \n'
                            '\\end{tikzpicture} }\n'

                                '}')


                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy \\\\ \n'
                        '\\hspace*{1cm} Nhánh ngoài cùng bên phải, từ trái sang phải đi lên nên $a>0$. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị cắt trục $Oy$ tại gốc tọa độ nên $d=0$. \\\\ \n'
                        'Gọi $x_1, x_2$ là hai điểm cực trị của hàm số, với $x_1 < x_2$, ta có \\\\ \n'
                        '\\hspace*{1cm} $0< x_1 < x_2$. \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2>0 \\Rightarrow -\\dfrac{b}{a} >0 \\Leftrightarrow \\dfrac{b}{a} <0$. Vì $a>0$ nên $b<0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 >0 \\Rightarrow \\dfrac{c}{a} >0$. Vì $a>0$ nên $c>0$. \\\\ \n'
                        'Vậy $a>0, b<0, c>0, d=0$.'
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='19':
                kq=1
                # Câu hỏi
                noidungcauhoi = ('\\immini{ '
                                'Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có đồ thị như hình vẽ. Trong các giá trị $a, b, c, d$ tìm các giá trị âm.'
                                '}{'                    
                                '\\scalebox{0.6}{ \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                            '\\tikzset{every node/.style={scale=0.9}} \n'
                            '\\draw[->] (-1.1,0)--(5.1,0) node[below left] {$x$}; \n'
                            '\\draw[->] (0,-3.1)--(0,3.1) node[below left] {$y$}; \n'
                            '\\draw (0,0) node [below left] {$O$}; \n'
                            '\\begin{scope} \n'
                            '\\clip (-1,-3) rectangle (5,3); \n'
                            '\\draw[samples=200,domain=-1:5,smooth,variable=\\x] plot (\\x,{1*((\\x)^3)+-6*((\\x)^2)+9*(\\x)+-2}); \n'
                            '\\end{scope} \n'
                            '\\end{tikzpicture} }\n'

                                '}')


                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy \\\\ \n'
                        '\\hspace*{1cm} Nhánh ngoài cùng bên phải, từ trái sang phải đi lên nên $a>0$. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị cắt trục $Oy$ tại điểm nằm phía dưới gốc tọa độ nên $d<0$. \\\\ \n'
                        'Gọi $x_1, x_2$ là hai điểm cực trị của hàm số, với $x_1 < x_2$, ta có \\\\ \n'
                        '\\hspace*{1cm} $0< x_1 < x_2$. \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2>0 \\Rightarrow -\\dfrac{b}{a} >0 \\Leftrightarrow \\dfrac{b}{a} <0$. Vì $a>0$ nên $b<0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 >0 \\Rightarrow \\dfrac{c}{a} >0$. Vì $a>0$ nên $c>0$. \\\\ \n'
                        'Vậy $a>0, b<0, c>0, d<0$.'
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='18':
                kq=2
                # Câu hỏi
                noidungcauhoi = ('\\immini{ '
                                'Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có đồ thị như hình vẽ. Trong các giá trị $a, b, c, d$ tìm các giá trị âm.'
                                '}{'                    
                                '\\scalebox{0.6}{ \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                            '\\tikzset{every node/.style={scale=0.9}} \n'
                            '\\draw[->] (-5.1,0)--(1.1,0) node[below left] {$x$}; \n'
                            '\\draw[->] (0,-3.1)--(0,3.1) node[below left] {$y$}; \n'
                            '\\draw (0,0) node [below right] {$O$}; \n'
                            '\\draw[dashed,thin](-3,0)--(-3,-2)--(0,-2); \n'
                            '\\draw[dashed,thin](-1,0)--(-1,2)--(0,2); \n'
                            '\\begin{scope} \n'
                            '\\clip (-5,-3) rectangle (1,3); \n'
                            '\\draw[samples=200,domain=-5:1,smooth,variable=\\x] plot (\\x,{-1*((\\x)^3)+-6*((\\x)^2)+-9*(\\x)+-2}); \n'
                            '\\end{scope} \n'
                            '\\end{tikzpicture}} \n'

                                '}')


                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy \\\\ \n'
                        '\\hspace*{1cm} Nhánh ngoài cùng bên phải, từ trái sang phải đi xuống nên $a<0$. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị cắt trục $Oy$ tại điểm nằm phía dưới gốc tọa độ nên $d<0$. \\\\ \n'
                        'Gọi $x_1, x_2$ là hai điểm cực trị của hàm số, với $x_1 < x_2$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1 < x_2 <0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2<0 \\Rightarrow -\\dfrac{b}{a} <0 \\Leftrightarrow \\dfrac{b}{a} >0$. Vì $a<0$ nên $b<0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 >0 \\Rightarrow \\dfrac{c}{a} >0$. Vì $a>0$ nên $c>0$. \\\\ \n'
                        'Vậy $a<0, b<0, c>0, d<0$.'
                        )

                #Đáp án
                dapan=' \\shortans[0]{$3$} '
            if dang=='17':
                kq=3
                # Câu hỏi
                noidungcauhoi = ('\\immini{ '
                                'Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có đồ thị như hình vẽ. Trong các giá trị $a, b, c, d$ tìm các giá trị âm.'
                                '}{'                    
                                '\\scalebox{0.6}{ \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                            '\\tikzset{every node/.style={scale=0.9}} \n'
                            '\\draw[->] (-5.1,0)--(1.1,0) node[below left] {$x$}; \n'
                            '\\draw[->] (0,-1.1)--(0,6.1) node[below left] {$y$}; \n'
                            '\\draw (0,0) node [below left] {$O$}; \n'
                            '\\draw[dashed,thin](-3,0)--(-3,1)--(0,1); \n'
                            '\\draw[dashed,thin](-1,0)--(-1,5)--(0,5); \n'
                            '\\begin{scope} \n'
                            '\\clip (-5,-1) rectangle (1,6); \n'
                            '\\draw[samples=200,domain=-5:1,smooth,variable=\\x] plot (\\x,{-1*((\\x)^3)+-6*((\\x)^2)+-9*(\\x)+1});  \n'
                            '\\end{scope} \n'
                            '\\end{tikzpicture} } \n'

                                '}')


                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy \\\\ \n'
                        '\\hspace*{1cm} Nhánh ngoài cùng bên phải, từ trái sang phải đi xuống nên $a<0$. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị cắt trục $Oy$ tại điểm nằm phía trên gốc tọa độ nên $d>0$. \\\\ \n'
                        'Gọi $x_1, x_2$ là hai điểm cực trị của hàm số, với $x_1 < x_2$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1 < x_2 <0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2<0 \\Rightarrow -\\dfrac{b}{a} <0 \\Leftrightarrow \\dfrac{b}{a} >0$. Vì $a<0$ nên $b<0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 >0 \\Rightarrow \\dfrac{c}{a} >0$. Vì $a<0$ nên $c<0$. \\\\ \n'
                        'Vậy $a<0, b<0, c<0, d>0$.'
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='16':
                kq=3
                # Câu hỏi
                noidungcauhoi = ('\\immini{ '
                                'Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có đồ thị như hình vẽ. Trong các giá trị $a, b, c, d$ tìm các giá trị âm.'
                                '}{'                    
                                '\\scalebox{0.6}{ \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                            '\\tikzset{every node/.style={scale=0.9}} \n'
                            '\\draw[->] (-5.1,0)--(1.1,0) node[below left] {$x$}; \n'
                            '\\draw[->] (0,-1.1)--(0,5.1) node[below left] {$y$}; \n'
                            '\\draw (0,0) node [below left] {$O$}; \n'
                            '\\draw[dashed,thin](-1,0)--(-1,4)--(0,4); \n'
                            '\\begin{scope} \n'
                            '\\clip (-5,-1) rectangle (1,5); \n'
                            '\\draw[samples=200,domain=-5:1,smooth,variable=\\x] plot (\\x,{-1*((\\x)^3)+-6*((\\x)^2)+-9*(\\x)+0}); \n'
                            '\\end{scope} \n'
                            '\\end{tikzpicture}} \n'

                                '}')


                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy \\\\ \n'
                        '\\hspace*{1cm} Nhánh ngoài cùng bên phải, từ trái sang phải đi xuống nên $a<0$. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị cắt trục $Oy$ tại gốc tọa độ nên $d=0$. \\\\ \n'
                        'Gọi $x_1, x_2$ là hai điểm cực trị của hàm số, với $x_1 < x_2$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1 < x_2 <0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2<0 \\Rightarrow -\\dfrac{b}{a} <0 \\Leftrightarrow \\dfrac{b}{a} >0$. Vì $a<0$ nên $b<0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 >0 \\Rightarrow \\dfrac{c}{a} >0$. Vì $a<0$ nên $c<0$. \\\\ \n'
                        'Vậy $a<0, b<0, c<0, d=0$.'
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            if dang=='15':
                kq=2
                # Câu hỏi
                noidungcauhoi = ('\\immini{ '
                                'Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có đồ thị như hình vẽ. Trong các giá trị $a, b, c, d$ tìm các giá trị dương.'
                                '}{'                    
                                '\\scalebox{0.6}{ \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]\n'
                            '\\tikzset{every node/.style={scale=0.9}}\n'
                            '\\draw[->] (-4.1,0)--(2.1,0) node[below left] {$x$};\n'
                            '\\draw[->] (0,-3.1)--(0,3.1) node[below left] {$y$};\n'
                            '\\draw (0,0) node [below left] {$O$};\n'
                            '\\draw[dashed,thin](-2,0)--(-2,-2)--(0,-2);\n'
                            '\\begin{scope}\n'
                            '\\clip (-4,-3) rectangle (2,3);\n'
                            '\\draw[samples=200,domain=-4:2,smooth,variable=\\x] plot (\\x,{-1*((\\x)^3)+-3*((\\x)^2)+0*(\\x)+2}); \n'
                            '\\end{scope}\n'
                            '\\end{tikzpicture} } \n'

                                '}')


                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy \\\\ \n'
                        '\\hspace*{1cm} Nhánh ngoài cùng bên phải, từ trái sang phải đi xuống nên $a<0$. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị cắt trục $Oy$ tại điểm nằm phía trên gốc tọa độ nên $d>0$. \\\\ \n'
                        'Gọi $x_1, x_2$ là hai điểm cực trị của hàm số, với $x_1 < x_2$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1 < x_2 =0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2<0 \\Rightarrow -\\dfrac{b}{a} <0 \\Leftrightarrow \\dfrac{b}{a} >0$. Vì $a<0$ nên $b<0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 =0 \\Rightarrow \\dfrac{c}{a} >0$. Vì $a>0$ nên $c=0$. \\\\ \n'
                        'Vậy $a<0, b<0, c=0, d>0$.'
                        )

                #Đáp án
                dapan=' \\shortans[0]{$1$} '

            if dang=='14':
                kq=0
                # Câu hỏi
                noidungcauhoi = ('\\immini{ '
                                'Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có đồ thị như hình vẽ. Trong các giá trị $a, b, c, d$ tìm các giá trị dương.'
                                '}{'                    
                                '\\scalebox{0.6}{ \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]\n'
                            '\\tikzset{every node/.style={scale=0.9}}\n'
                            '\\draw[->] (-4.1,0)--(2.1,0) node[below left] {$x$};\n'
                            '\\draw[->] (0,-6.1)--(0,1.1) node[below left] {$y$};\n'
                            '\\draw (0,0) node [below left] {$O$};\n'
                            '\\draw[dashed,thin](-2,0)--(-2,-5)--(0,-5);\n'
                            '\\begin{scope}\n'
                            '\\clip (-4,-6) rectangle (2,1);\n'
                            '\\draw[samples=200,domain=-4:2,smooth,variable=\\x] plot (\\x,{-1*((\\x)^3)+-3*((\\x)^2)+0*(\\x)+-1}); \n'
                            '\\end{scope}\n'
                            '\\end{tikzpicture} } \n'

                                '}')


                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy \\\\ \n'
                        '\\hspace*{1cm} Nhánh ngoài cùng bên phải, từ trái sang phải đi xuống nên $a<0$. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị cắt trục $Oy$ tại điểm nằm phía dưới gốc tọa độ nên $d<0$. \\\\ \n'
                        'Gọi $x_1, x_2$ là hai điểm cực trị của hàm số, với $x_1 < x_2$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1 < x_2 =0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2<0 \\Rightarrow -\\dfrac{b}{a} <0 \\Leftrightarrow \\dfrac{b}{a} >0$. Vì $a<0$ nên $b<0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 =0 \\Rightarrow \\dfrac{c}{a} =0$. Vì $a<0$ nên $c=0$. \\\\ \n'
                        'Vậy $a<0, b<0, c=0, d<0$.'
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='13':
                kq=0
                # Câu hỏi
                noidungcauhoi = ('\\immini{ '
                                'Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có đồ thị như hình vẽ. Trong các giá trị $a, b, c, d$ tìm các giá trị dương.'
                                '}{'                    
                                '\\scalebox{0.6}{ \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                            '\\tikzset{every node/.style={scale=0.9}} \n'
                            '\\draw[->] (-4.1,0)--(2.1,0) node[below left] {$x$}; \n'
                            '\\draw[->] (0,-5.1)--(0,1.1) node[below left] {$y$}; \n'
                            '\\draw (0,0) node [above left] {$O$}; \n'
                            '\\draw[dashed,thin](-2,0)--(-2,-4)--(0,-4); \n'
                            '\\begin{scope} \n'
                            '\\clip (-4,-5) rectangle (2,1); \n'
                            '\\draw[samples=200,domain=-4:2,smooth,variable=\\x] plot (\\x,{-1*((\\x)^3)+-3*((\\x)^2)+0*(\\x)+0});  \n'
                            '\\end{scope} \n'
                            '\\end{tikzpicture} }\n'

                                '}')


                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy \\\\ \n'
                        '\\hspace*{1cm} Nhánh ngoài cùng bên phải, từ trái sang phải đi xuống nên $a<0$. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị cắt trục $Oy$ tại gốc tọa độ nên $d=0$. \\\\ \n'
                        'Gọi $x_1, x_2$ là hai điểm cực trị của hàm số, với $x_1 < x_2$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1 < x_2 =0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2<0 \\Rightarrow -\\dfrac{b}{a} <0 \\Leftrightarrow \\dfrac{b}{a} >0$. Vì $a<0$ nên $b<0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 =0 \\Rightarrow \\dfrac{c}{a} =0$. Vì $a<0$ nên $c=0$. \\\\ \n'
                        'Vậy $a<0, b<0, c=0, d=0$.'
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            if dang=='12':
                kq=2
                # Câu hỏi
                noidungcauhoi = ('\\immini{ '
                                'Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có đồ thị như hình vẽ. Trong các giá trị $a, b, c, d$ tìm các giá trị dương.'
                                '}{'                    
                                '\\scalebox{0.6}{ \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                            '\\tikzset{every node/.style={scale=0.9}} \n'
                            '\\draw[->] (-3.1,0)--(2.1,0) node[below left] {$x$}; \n'
                            '\\draw[->] (0,-3.1)--(0,3.1) node[below left] {$y$}; \n'
                            '\\draw (0,0) node [below left] {$O$}; \n'
                            '\\draw[dashed,thin](-1.5,0)--(-1.5,-2)--(0,-2); \n'
                            '\\draw[dashed,thin](0.5,0)--(0.5,2)--(0,2); \n'
                            '\\begin{scope} \n'
                            '\\clip (-3,-3) rectangle (2,3); \n'
                            '\\draw[samples=200,domain=-3:2,smooth,variable=\\x] plot (\\x,{-1*((\\x)^3)+-1.5*((\\x)^2)+2.25*(\\x)+1.375});  \n'
                            '\\end{scope} \n'
                            '\\end{tikzpicture} }\n'

                                '}')


                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy \\\\ \n'
                        '\\hspace*{1cm} Nhánh ngoài cùng bên phải, từ trái sang phải đi xuống nên $a<0$. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị cắt trục $Oy$ tại điểm nằm phía trên gốc tọa độ nên $d>0$. \\\\ \n'
                        'Gọi $x_1, x_2$ là hai điểm cực trị của hàm số, với $x_1 < x_2$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1 <0< x_2$ và $\\abs{x_1}>\\abs{x2}$. \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2<0 \\Rightarrow -\\dfrac{b}{a} <0 \\Leftrightarrow \\dfrac{b}{a} >0$. Vì $a<0$ nên $b<0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 <0 \\Rightarrow \\dfrac{c}{a} <0$. Vì $a>0$ nên $c<0$. \\\\ \n'
                        'Vậy $a<0, b<0, c<0, d>0$.'
                        )

                #Đáp án
                dapan=' \\shortans[0]{$1$} '
            if dang=='11':
                kq=1
                # Câu hỏi
                noidungcauhoi = ('\\immini{ '
                                'Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có đồ thị như hình vẽ. Trong các giá trị $a, b, c, d$ tìm các giá trị dương.'
                                '}{'                    
                                '\\scalebox{0.6}{ \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                            '\\tikzset{every node/.style={scale=0.9}} \n'
                            '\\draw[->] (-3.1,0)--(2.1,0) node[below left] {$x$}; \n'
                            '\\draw[->] (0,-6.1)--(0,1.1) node[below left] {$y$}; \n'
                            '\\draw (0,0) node [below left] {$O$}; \n'
                            '\\draw[dashed,thin](-1.5,0)--(-1.5,-5)--(0,-5); \n'
                            '\\draw[dashed,thin](0.5,0)--(0.5,-1)--(0,-1); \n'
                            '\\begin{scope} \n'
                            '\\clip (-3,-6) rectangle (2,1); \n'
                            '\\draw[samples=200,domain=-3:2,smooth,variable=\\x] plot (\\x,{-1*((\\x)^3)+-1.5*((\\x)^2)+2.25*(\\x)+-1.6});  \n'
                            '\\end{scope} \n'
                            '\\end{tikzpicture} }\n'

                                '}')


                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy \\\\ \n'
                        '\\hspace*{1cm} Nhánh ngoài cùng bên phải, từ trái sang phải đi xuống nên $a<0$. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị cắt trục $Oy$ tại điểm nằm phía dưới gốc tọa độ nên $d<0$. \\\\ \n'
                        'Gọi $x_1, x_2$ là hai điểm cực trị của hàm số, với $x_1 < x_2$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1 <0< x_2$ và $\\abs{x_1}>\\abs{x2}$. \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2<0 \\Rightarrow -\\dfrac{b}{a} <0 \\Leftrightarrow \\dfrac{b}{a} >0$. Vì $a<0$ nên $b<0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 <0 \\Rightarrow \\dfrac{c}{a} <0$. Vì $a>0$ nên $c<0$. \\\\ \n'
                        'Vậy $a<0, b<0, c<0, d<0$.'
                        )

                #Đáp án
                dapan=' \\shortans[0]{$0$} '
            if dang=='10':
                kq=2
                # Câu hỏi
                noidungcauhoi = ('\\immini{ '
                                'Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có đồ thị như hình vẽ. Trong các giá trị $a, b, c, d$ tìm các giá trị âm.'
                                '}{'                    
                                '\\scalebox{0.6}{ \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                            '\\tikzset{every node/.style={scale=0.9}} \n'
                            '\\draw[->] (-3.1,0)--(2.1,0) node[below left] {$x$}; \n'
                            '\\draw[->] (0,-4.1)--(0,1.1) node[below left] {$y$}; \n'
                            '\\draw (0,0) node [below left] {$O$}; \n'
                            '\\draw[dashed,thin](-1.5,0)--(-1.5,-3.4)--(0,-3.4); \n'
                            '\\draw[dashed,thin](0.5,0)--(0.5,0.6)--(0,0.6); \n'
                            '\\begin{scope} \n'
                            '\\clip (-3,-4) rectangle (2,1); \n'
                            '\\draw[samples=200,domain=-3:2,smooth,variable=\\x] plot (\\x,{-1*((\\x)^3)+-1.5*((\\x)^2)+2.25*(\\x)+0});  \n'
                            '\\end{scope} \n'
                            '\\end{tikzpicture} } \n'

                                '}')


                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy \\\\ \n'
                        '\\hspace*{1cm} Nhánh ngoài cùng bên phải, từ trái sang phải đi xuống nên $a<0$. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị cắt trục $Oy$ tại gốc tọa độ nên $d=0$. \\\\ \n'
                        'Gọi $x_1, x_2$ là hai điểm cực trị của hàm số, với $x_1 < x_2$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1 <0< x_2$ và $\\abs{x_1}>\\abs{x2}$. \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2<0 \\Rightarrow -\\dfrac{b}{a} <0 \\Leftrightarrow \\dfrac{b}{a} >0$. Vì $a<0$ nên $b<0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 <0 \\Rightarrow \\dfrac{c}{a} <0$. Vì $a>0$ nên $c<0$. \\\\ \n'
                        'Vậy $a<0, b<0, c<0, d=0$.'
                        )

                #Đáp án
                dapan=' \\shortans[0]{$3$} '

            if dang=='9':
                kq=1
                # Câu hỏi
                noidungcauhoi = ('\\immini{ '
                                'Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có đồ thị như hình vẽ. Trong các giá trị $a, b, c, d$ tìm các giá trị âm.'
                                '}{'                    
                                '\\scalebox{0.6}{ \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]\n'
                            '\\tikzset{every node/.style={scale=0.9}}\n'
                            '\\draw[->] (-2.1,0)--(3.1,0) node[below left] {$x$};\n'
                            '\\draw[->] (0,-1.1)--(0,5.1) node[below left] {$y$};\n'
                            '\\draw (0,0) node [below left] {$O$};\n'
                            '\\draw[dashed,thin](1.5,0)--(1.5,4)--(0,4);\n'
                            '\\begin{scope}\n'
                            '\\clip (-2,-1) rectangle (3,5);\n'
                            '\\draw[samples=200,domain=-2:3,smooth,variable=\\x] plot (\\x,{-1*((\\x)^3)+1.5*((\\x)^2)+2.25*(\\x)+0.625});  \n'
                            '\\end{scope}\n'
                            '\\end{tikzpicture} } \n'

                                '}')


                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy \\\\ \n'
                        '\\hspace*{1cm} Nhánh ngoài cùng bên phải, từ trái sang phải đi xuống nên $a<0$. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị cắt trục $Oy$ tại điểm nằm phía trên gốc tọa độ nên $d>0$. \\\\ \n'
                        'Gọi $x_1, x_2$ là hai điểm cực trị của hàm số, với $x_1 < x_2$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1 <0< x_2$ và $\\abs{x_1}<\\abs{x_2}$. \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2>0 \\Rightarrow -\\dfrac{b}{a} >0 \\Leftrightarrow \\dfrac{b}{a} <0$. Vì $a<0$ nên $b>0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 <0 \\Rightarrow \\dfrac{c}{a} <0$. Vì $a<0$ nên $c>0$. \\\\ \n'
                        'Vậy $a<0, b>0, c>0, d>0$.'
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            if dang=='8':
                kq=4
                # Câu hỏi
                noidungcauhoi = ('\\immini{ '
                                'Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có đồ thị như hình vẽ. Trong các giá trị $a, b, c, d$ tìm các giá trị âm.'
                                '}{'                    
                                '\\scalebox{0.6}{ \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                            '\\tikzset{every node/.style={scale=0.9}} \n'
                            '\\draw[->] (-2.1,0)--(3.1,0) node[below left] {$x$}; \n'
                            '\\draw[->] (0,-3.1)--(0,3.1) node[below left] {$y$}; \n'
                            '\\draw (0,0) node [below left] {$O$}; \n'
                            '\\draw[dashed,thin](-0.5,0)--(-0.5,-2)--(0,-2); \n'
                            '\\draw[dashed,thin](1.5,0)--(1.5,2)--(0,2); \n'
                            '\\begin{scope} \n'
                            '\\clip (-2,-3) rectangle (3,3); \n'
                            '\\draw[samples=200,domain=-2:3,smooth,variable=\\x] plot (\\x,{-1*((\\x)^3)+1.5*((\\x)^2)+2.25*(\\x)+-1.35});  \n'
                            '\\end{scope} \n'
                            '\\end{tikzpicture}} \n'

                                '}')


                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy \\\\ \n'
                        '\\hspace*{1cm} Nhánh ngoài cùng bên phải, từ trái sang phải đi xuống nên $a<0$. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị cắt trục $Oy$ tại điểm nằm phía dưới gốc tọa độ nên $d<0$. \\\\ \n'
                        'Gọi $x_1, x_2$ là hai điểm cực trị của hàm số, với $x_1 < x_2$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1 <0< x_2$ và $\\abs{x_1}<\\abs{x2}$. \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2>0 \\Rightarrow -\\dfrac{b}{a} >0 \\Leftrightarrow \\dfrac{b}{a} <0$. Vì $a<0$ nên $b>0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 <0 \\Rightarrow \\dfrac{c}{a} <0$. Vì $a>0$ nên $c<0$. \\\\ \n'
                        'Vậy $a<0, b>0, c<0, d<0$.'
                        )

                #Đáp án
                dapan=' \\shortans[0]{$3$} '
            if dang=='7':
                kq=1
                # Câu hỏi
                noidungcauhoi = ('\\immini{ '
                                'Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có đồ thị như hình vẽ. Trong các giá trị $a, b, c, d$ tìm các giá trị âm.'
                                '}{'                    
                                '\\scalebox{0.6}{ \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                            '\\tikzset{every node/.style={scale=0.9}} \n'
                            '\\draw[->] (-2.1,0)--(3.1,0) node[below left] {$x$}; \n'
                            '\\draw[->] (0,-1.1)--(0,4.1) node[below left] {$y$}; \n'
                            '\\draw (0,0) node [above left] {$O$}; \n'
                            '\\draw[dashed,thin](-0.5,0)--(-0.5,-0.6)--(0,-0.6); \n'
                            '\\draw[dashed,thin](1.5,0)--(1.5,3.4)--(0,3.4); \n'
                            '\\begin{scope} \n'
                            '\\clip (-2,-1) rectangle (3,4); \n'
                            '\\draw[samples=200,domain=-2:3,smooth,variable=\\x] plot (\\x,{-1*((\\x)^3)+1.5*((\\x)^2)+2.25*(\\x)+0});  \n'
                            '\\end{scope} \n'
                            '\\end{tikzpicture}} \n'

                                '}')


                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy \\\\ \n'
                        '\\hspace*{1cm} Nhánh ngoài cùng bên phải, từ trái sang phải đi xuống nên $a<0$. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị cắt trục $Oy$ tại gốc tọa độ nên $d=0$. \\\\ \n'
                        'Gọi $x_1, x_2$ là hai điểm cực trị của hàm số, với $x_1 < x_2$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1 <0< x_2$ và $\\abs{x_1}<\\abs{x2}$. \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2>0 \\Rightarrow -\\dfrac{b}{a} >0 \\Leftrightarrow \\dfrac{b}{a} <0$. Vì $a<0$ nên $b>0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 <0 \\Rightarrow \\dfrac{c}{a} <0$. Vì $a<0$ nên $c>0$. \\\\ \n'
                        'Vậy $a<0, b>0, c>0, d=0$.'
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            if dang=='6':
                kq=1
                # Câu hỏi
                noidungcauhoi = ('\\immini{ '
                                'Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có đồ thị như hình vẽ. Trong các giá trị $a, b, c, d$ tìm các giá trị dương.'
                                '}{'                    
                                '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-2.1,0)--(4.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,-1.1)--(0,6.1) node[below left] {$y$}; \n'
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw[dashed,thin](2,0)--(2,5)--(0,5); \n'
                                '\\begin{scope} \n'
                                '\\clip (-2,-1) rectangle (4,6); \n'
                                '\\draw[samples=200,domain=-2:4,smooth,variable=\\x] plot (\\x,{-1*((\\x)^3)+3*((\\x)^2)+0*(\\x)+1});  \n'
                                '\\end{scope} \n'
                                '\\end{tikzpicture} }\n'

                                '}')


                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy \\\\ \n'
                        '\\hspace*{1cm} Nhánh ngoài cùng bên phải, từ trái sang phải đi xuống nên $a<0$. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị cắt trục $Oy$ tại điểm nằm phía trên gốc tọa độ nên $d>0$. \\\\ \n'
                        'Gọi $x_1, x_2$ là hai điểm cực trị của hàm số, với $x_1 < x_2$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1 =0< x_2$. \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2>0 \\Rightarrow -\\dfrac{b}{a} >0 \\Leftrightarrow \\dfrac{b}{a} <0$. Vì $a<0$ nên $b>0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 =0 \\Rightarrow \\dfrac{c}{a} =0$. Vì $a>0$ nên $c=0$. \\\\ \n'
                        'Vậy $a<0, b>0, c=0, d>0$.'
                        )

                #Đáp án
                dapan=' \\shortans[0]{$2$} '

            if dang=='5':
                kq=3
                # Câu hỏi
                noidungcauhoi = ('\\immini{ '
                                'Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có đồ thị như hình vẽ. Trong các giá trị $a, b, c, d$ tìm các giá trị dương.'
                                '}{'                    
                                '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-2.1,0)--(4.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,-2.1)--(0,4.1) node[below left] {$y$}; \n'
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw[dashed,thin](2,0)--(2,3)--(0,3); \n'
                                '\\begin{scope} \n'
                                '\\clip (-2,-2) rectangle (4,4); \n'
                                '\\draw[samples=200,domain=-2:4,smooth,variable=\\x] plot (\\x,{-1*((\\x)^3)+3*((\\x)^2)+0*(\\x)+-1});  \n'
                                '\\end{scope} \n'
                                '\\end{tikzpicture} } \n'

                                '}')


                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy \\\\ \n'
                        '\\hspace*{1cm} Nhánh ngoài cùng bên phải, từ trái sang phải đi xuống nên $a<0$. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị cắt trục $Oy$ tại điểm nằm phía dưới gốc tọa độ nên $d<0$. \\\\ \n'
                        'Gọi $x_1, x_2$ là hai điểm cực trị của hàm số, với $x_1 < x_2$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1 =0< x_2$. \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2>0 \\Rightarrow -\\dfrac{b}{a} >0 \\Leftrightarrow \\dfrac{b}{a} <0$. Vì $a<0$ nên $b>0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 =0 \\Rightarrow \\dfrac{c}{a} =0$. Vì $a>0$ nên $c=0$. \\\\ \n'
                        'Vậy $a<0, b>0, c=0, d<0$.'
                        )

                #Đáp án
                dapan=' \\shortans[0]{$1$} '

            if dang=='4':
                kq=2
                # Câu hỏi
                noidungcauhoi = ('\\immini{ '
                                'Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có đồ thị như hình vẽ. Trong các giá trị $a, b, c, d$ tìm các giá trị âm.'
                                '}{'                    
                                '\\scalebox{0.6}{ \n'
                            '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                            '\\tikzset{every node/.style={scale=0.9}} \n'
                            '\\draw[->] (-2.1,0)--(4.1,0) node[below left] {$x$}; \n'
                            '\\draw[->] (0,-1.1)--(0,5.1) node[below left] {$y$}; \n'
                            '\\draw (0,0) node [below left] {$O$}; \n'
                            '\\draw[dashed,thin](2,0)--(2,4)--(0,4); \n'
                            '\\begin{scope} \n'
                            '\\clip (-2,-1) rectangle (4,5); \n'
                            '\\draw[samples=200,domain=-2:4,smooth,variable=\\x] plot (\\x,{-1*((\\x)^3)+3*((\\x)^2)+0*(\\x)+0});  \n'
                            '\\end{scope} \n'
                            '\\end{tikzpicture} }\n'

                                '}')


                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy \\\\ \n'
                        '\\hspace*{1cm} Nhánh ngoài cùng bên phải, từ trái sang phải đi xuống nên $a<0$. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị cắt trục $Oy$ tại gốc tọa độ nên $d=0$. \\\\ \n'
                        'Gọi $x_1, x_2$ là hai điểm cực trị của hàm số, với $x_1 < x_2$, ta có \\\\ \n'
                        '\\hspace*{1cm} $x_1 =0< x_2$. \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2>0 \\Rightarrow -\\dfrac{b}{a} >0 \\Leftrightarrow \\dfrac{b}{a} <0$. Vì $a<0$ nên $b>0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 =0 \\Rightarrow \\dfrac{c}{a} =0$. Vì $a>0$ nên $c=0$. \\\\ \n'
                        'Vậy $a<0, b>0, c=0, d=0$.'
                        )

                #Đáp án
                dapan=' \\shortans[0]{$1$} '

            if dang=='3':
                kq=2
                # Câu hỏi
                noidungcauhoi = ('\\immini{ '
                                'Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có đồ thị như hình vẽ. Trong các giá trị $a, b, c, d$ tìm các giá trị dương.'
                                '}{'                    
                                '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-1.1,0)--(5.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,-1.1)--(0,6.1) node[below left] {$y$}; \n'
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw[dashed,thin](1,0)--(1,1)--(0,1); \n'
                                '\\draw[dashed,thin](3,0)--(3,5)--(0,5); \n'
                                '\\begin{scope} \n'
                                '\\clip (-1,-1) rectangle (5,6); \n'
                                '\\draw[samples=200,domain=-1:5,smooth,variable=\\x] plot (\\x,{-1*((\\x)^3)+6*((\\x)^2)+-9*(\\x)+5});  \n'
                                '\\end{scope} \n'
                                '\\end{tikzpicture} }\n'

                                '}')


                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy \\\\ \n'
                        '\\hspace*{1cm} Nhánh ngoài cùng bên phải, từ trái sang phải đi xuống nên $a<0$. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị cắt trục $Oy$ tại điểm nằm phía trên gốc tọa độ nên $d>0$. \\\\ \n'
                        'Gọi $x_1, x_2$ là hai điểm cực trị của hàm số, với $x_1 < x_2$, ta có \\\\ \n'
                        '\\hspace*{1cm} $0< x_1 < x_2$. \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2>0 \\Rightarrow -\\dfrac{b}{a} >0 \\Leftrightarrow \\dfrac{b}{a} <0$. Vì $a<0$ nên $b>0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 >0 \\Rightarrow \\dfrac{c}{a} >0$. Vì $a>0$ nên $c>0$. \\\\ \n'
                        'Vậy $a<0, b>0, c>0, d>0$.'
                        )

                #Đáp án
                dapan=' \\shortans[0]{$3$} '

            if dang=='2':
                kq=3
                # Câu hỏi
                noidungcauhoi = ('\\immini{ '
                                'Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có đồ thị như hình vẽ. Trong các giá trị $a, b, c, d$ tìm các giá trị âm.'
                                '}{'                    
                                '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-1.1,0)--(5.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,-6.1)--(0,1.1) node[below right] {$y$}; \n'
                                '\\draw (0,0) node [below right] {$O$}; \n'
                                '\\draw[dashed,thin](1,0)--(1,-5)--(0,-5); \n'
                                '\\draw[dashed,thin](3,0)--(3,-1)--(0,-1); \n'
                                '\\begin{scope} \n'
                                '\\clip (-1,-6) rectangle (5,1); \n'
                                '\\draw[samples=200,domain=-1:5,smooth,variable=\\x] plot (\\x,{-1*((\\x)^3)+6*((\\x)^2)+-9*(\\x)+-1});  \n'
                                '\\end{scope} \n'
                                '\\end{tikzpicture}} \n'

                                '}')


                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy \\\\ \n'
                        '\\hspace*{1cm} Nhánh ngoài cùng bên phải, từ trái sang phải đi xuống nên $a<0$. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị cắt trục $Oy$ tại điểm nằm phía dưới gốc tọa độ nên $d<0$. \\\\ \n'
                        'Gọi $x_1, x_2$ là hai điểm cực trị của hàm số, với $x_1 < x_2$, ta có \\\\ \n'
                        '\\hspace*{1cm} $0< x_1 < x_2$. \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2>0 \\Rightarrow -\\dfrac{b}{a} >0 \\Leftrightarrow \\dfrac{b}{a} <0$. Vì $a<0$ nên $b>0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 >0 \\Rightarrow \\dfrac{c}{a} >0$. Vì $a<0$ nên $c<0$. \\\\ \n'
                        'Vậy $a<0, b>0, c<0, d<0$.'
                        )

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            if dang=='1':
                kq=1
                # Câu hỏi
                noidungcauhoi = ('\\immini{ '
                                'Cho hàm số $y=ax^3+bx^2+cx+d$ với $a, b, c, d \\in \\mathbb{R}$ có đồ thị như hình vẽ. Trong các giá trị $a, b, c, d$ tìm các giá trị dương.'
                                '}{'                    
                                '\\scalebox{0.6}{ \n'
                                '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] \n'
                                '\\tikzset{every node/.style={scale=0.9}} \n'
                                '\\draw[->] (-1.1,0)--(5.1,0) node[below left] {$x$}; \n'
                                '\\draw[->] (0,-5.1)--(0,1.1) node[below left] {$y$}; \n'
                                '\\draw (0,0) node [below left] {$O$}; \n'
                                '\\draw[dashed,thin](1,0)--(1,-4)--(0,-4); \n'
                                '\\begin{scope} \n'
                                '\\clip (-1,-5) rectangle (5,1); \n'
                                '\\draw[samples=200,domain=-1:5,smooth,variable=\\x] plot (\\x,{-1*((\\x)^3)+6*((\\x)^2)+-9*(\\x)+0});  \n'
                                '\\end{scope} \n'
                                '\\end{tikzpicture} }\n'

                                '}')


                # Nội dung lời giải
                loigiai=(
                        'Từ hình vẽ ta thấy \\\\ \n'
                        '\\hspace*{1cm} Nhánh ngoài cùng bên phải, từ trái sang phải đi xuống nên $a<0$. \\\\ \n'
                        '\\hspace*{1cm} Đồ thị cắt trục $Oy$ tại gốc tọa độ nên $d=0$. \\\\ \n'
                        'Gọi $x_1, x_2$ là hai điểm cực trị của hàm số, với $x_1 < x_2$, ta có \\\\ \n'
                        '\\hspace*{1cm} $0< x_1 < x_2$. \\\\ \n'
                        '\\hspace*{1cm} $x_1+x_2>0 \\Rightarrow -\\dfrac{b}{a} >0 \\Leftrightarrow \\dfrac{b}{a} <0$. Vì $a<0$ nên $b>0$. \\\\ \n'
                        '\\hspace*{1cm} $x_1 \\cdot x_2 >0 \\Rightarrow \\dfrac{c}{a} >0$. Vì $a<0$ nên $c<0$. \\\\ \n'
                        'Vậy $a<0, b>0, c<0, d=0$.'
                        )

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

