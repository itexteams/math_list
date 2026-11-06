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


def bt_dang9_p2_b1_c4_ds11(self):
            # Khai báo biến
            # Khai báo biến
            n = symbols('n')
            k = 5 # Số hình vuông giữ lại
            d = 3 # Tỉ lệ chia cạnh

            # Random cạnh ban đầu L của hình vuông H0
            L = randint(1, 9) 

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Xét quá trình tạo ra hình vuông như sau: 
                             \begin{center}
                             \scalebox{0.6}{ 
            	\tikzset{every picture/.style={line width=0.75pt}}        
            	\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (0,0) -- (150,0) -- (150,150) -- (0,150) -- cycle ;
            		\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (200,0) -- (250,0) -- (250,50) -- (200,50) -- cycle ;
            		\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (300,0) -- (350,0) -- (350,50) -- (300,50) -- cycle ;
            		\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (250,50) -- (300,50) -- (300,100) -- (250,100) -- cycle ;
            		\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (200,100) -- (250,100) -- (250,150) -- (200,150) -- cycle ;
            		\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (300,100) -- (350,100) -- (350,150) -- (300,150) -- cycle ;
            		\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (400,0) -- (416.67,0) -- (416.67,16.67) -- (400,16.67) -- cycle ; 
            		\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (433.33,0) -- (450,0) -- (450,16.67) -- (433.33,16.67) -- cycle ;
            		\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (416.67,16.67) -- (433.33,16.67) -- (433.33,33.33) -- (416.67,33.33) -- cycle ;
            		\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (400,33.33) -- (416.67,33.33) -- (416.67,50) -- (400,50) -- cycle ;
            		\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (433.33,33.33) -- (450,33.33) -- (450,50) -- (433.33,50) -- cycle ;
            		\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (500,0) -- (516.67,0) -- (516.67,16.67) -- (500,16.67) -- cycle ;
            		\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (533.33,0) -- (550,0) -- (550,16.67) -- (533.33,16.67) -- cycle ;
            		\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (516.67,16.67) -- (533.33,16.67) -- (533.33,33.33) -- (516.67,33.33) -- cycle ;
            		\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (500,33.33) -- (516.67,33.33) -- (516.67,50) -- (500,50) -- cycle ;
            		\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (533.33,33.33) -- (550,33.33) -- (550,50) -- (533.33,50) -- cycle ;
            		\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (450,50) -- (466.67,50) -- (466.67,66.67) -- (450,66.67) -- cycle ;
            		\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (483.33,50) -- (500,50) -- (500,66.67) -- (483.33,66.67) -- cycle ;
            		\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (466.67,66.67) -- (483.33,66.67) -- (483.33,83.33) -- (466.67,83.33) -- cycle ;
            		\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (450,83.33) -- (466.67,83.33) -- (466.67,100) -- (450,100) -- cycle ;
            		\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (483.33,83.33) -- (500,83.33) -- (500,100) -- (483.33,100) -- cycle ;
            		\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (400,100) -- (416.67,100) -- (416.67,116.67) -- (400,116.67) -- cycle ;
            		\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (433.33,100) -- (450,100) -- (450,116.67) -- (433.33,116.67) -- cycle ;
            		\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (416.67,116.67) -- (433.33,116.67) -- (433.33,133.33) -- (416.67,133.33) -- cycle ;
            		\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (400,133.33) -- (416.67,133.33) -- (416.67,150) -- (400,150) -- cycle ;
            		\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (433.33,133.33) -- (450,133.33) -- (450,150) -- (433.33,150) -- cycle ;
            		\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (500,100) -- (516.67,100) -- (516.67,116.67) -- (500,116.67) -- cycle ;
            		\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (533.33,100) -- (550,100) -- (550,116.67) -- (533.33,116.67) -- cycle ;
            		\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (516.67,116.67) -- (533.33,116.67) -- (533.33,133.33) -- (516.67,133.33) -- cycle ;
            		\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (500,133.33) -- (516.67,133.33) -- (516.67,150) -- (500,150) -- cycle ;
            		\draw  [fill={rgb, 255:red, 184; green, 233; blue, 134 }  ,fill opacity=1 ] (533.33,133.33) -- (550,133.33) -- (550,150) -- (533.33,150) -- cycle ;
            		\draw (59,158) node [anchor=north west][inner sep=0.75pt]    {$H_{0}$};
            		\draw (265,159) node [anchor=north west][inner sep=0.75pt]    {$H_{1}$};
            		\draw (465,159) node [anchor=north west][inner sep=0.75pt]    {$H_{2}$};
            	\end{tikzpicture} }
            \end{center}
                             Bắt đầu bằng một hình vuông $H_0$ cạnh bằng $%s$ đơn vị độ dài. Chia hình vuông $H_0$ thành chín hình vuông bằng nhau, bỏ đi bốn hình vuông, nhận được hình $H_1$. Tiếp theo, chia mỗi hình vuông của $H_1$ thành chín hình vuông rồi bỏ đi bốn hình vuông, nhận được hình $H_2$. Tiếp tục quá trình này, ta nhận được một dãy hình $H_n$ ($n=1,2,3,...$). Xét $u_n$ là cạnh của mỗi hình vuông tương ứng với hình $H_n$.''' 
                             % (latex(L)))

            ########################################################################
            # Nhận biết
            nb_da_1_d = r'\True $H_1$ có %s hình vuông, mỗi hình vuông có cạnh bằng $u_1 = %s$' % (k, latex(Rational(L, d)))
            nb_da_1_s = r'$H_1$ có 4 hình vuông, mỗi hình vuông có cạnh bằng $u_1 = %s$' % (latex(Rational(L, d)))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = (r'''Hình $H_1$ được tạo ra bằng cách chia cạnh $H_0$ làm 3, nên cạnh $u_1 = %s$. Theo đề bài, ta giữ lại $5$ hình vuông nên $H_1$ có $5$ hình vuông.''' 
                            % (latex(Rational(L, d))))

            ########################################################################
            # Thông hiểu
            th_da_1_d = r'\True $H_2$ có $5^2$ hình vuông, mỗi hình vuông có cạnh bằng $u_2 = %s$' % (latex(Rational(L, d**2)))
            th_da_1_s = r'$H_2$ có $5^2$ hình vuông, mỗi hình vuông có cạnh bằng $u_2 = %s$' % (latex(Rational(L, d)))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = (r'''Mỗi hình vuông ở $H_1$ lại được chia làm 9 và giữ lại 5, nên số hình vuông là $5 \times 5 = 5^2$. Cạnh mỗi hình vuông tiếp tục chia 3 nên $u_2 = \frac{u_1}{3} = %s$.''' 
                            % (latex(Rational(L, d**2))))

            ########################################################################
            # Vận dụng - SỬA LỖI TẠI ĐÂY
            # Thay Rational(L, d**n) bằng L / d**n
            vd_da_1_d = r'\True Cạnh $u_n = %s$ là một cấp số nhân lùi vô hạn với công bội $q = \frac{1}{3}$' % (latex(L / d**n))
            vd_da_1_s = r'Cạnh $u_n = %s$ là một cấp số nhân với công bội $q = \frac{5}{9}$' % (latex(L / d**n))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = (r'''Qua mỗi bước, cạnh của hình vuông giảm đi 3 lần, do đó $u_n = \frac{%s}{3^n} = %s$. Đây là CSN có $u_1 = %s$ và $q = \frac{1}{3}$. Vì $|q| < 1$ nên là CSN lùi vô hạn.''' 
                            % (L, latex(L / d**n), latex(Rational(L, d))))

            ########################################################################
            # Vận dụng cao
            vdc_da_1_d = r'\True Diện tích $S_n$ của $H_n$ là $S_n = %s \cdot \left(\frac{5}{9}\right)^n$ và $\lim S_n = 0$' % (latex(L**2) if L**2 != 1 else "")
            vdc_da_1_s = r'Diện tích $S_n$ của $H_n$ là $S_n = %s \cdot \left(\frac{5}{9}\right)^n$ và $\lim S_n = +\infty$' % (latex(L**2) if L**2 != 1 else "")
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = (r'''Diện tích mỗi hình vuông nhỏ ở bước $n$ là $u_n^2 = \left(\frac{%s}{3^n}\right)^2$. Số lượng hình vuông là $5^n$. \\ Vậy $S_n = 5^n \cdot \frac{%s}{9^n} = %s \cdot \left(\frac{5}{9}\right)^n$. \\ Vì $0 < \frac{5}{9} < 1$ nên $\lim S_n = 0$.''' 
                             % (L, L**2, L**2))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Logic xáo trộn
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([nb_da_1, th_da_1, vd_da_1, vdc_da_1]) <= 3:
                    break

            # Xuất kết quả
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(nb_da_1) + '}\n'
                '{' + str(th_da_1) + '}\n'
                '{' + str(vd_da_1) + '}\n'
                '{' + str(vdc_da_1) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

