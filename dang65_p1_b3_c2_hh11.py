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


def bt_dang65_p1_b3_c2_hh11(self):
            # Khai báo biến
            # Cạnh a của hình lập phương có thể thay đổi từ 1 đến 10
            a = random.randint(1, 10)

            # B2-Viết lại bài toán
            noidungcauhoi = ('''Cho hình lập phương $ABCD.A'B'C'D'$ có cạnh bằng $%s$. Giá trị $\\sin$ của góc giữa đường thẳng $AC'$ và mặt phẳng $(ABCD)$ bằng'''
                             %(latex(a)))

            # Tính toán đáp án
            # sin(phi) = CC'/AC' = a / (a*sqrt(3)) = 1/sqrt(3) = sqrt(3)/3
            # Đáp án đúng là sqrt(3)/3
            da = '$\\frac{\\sqrt{3}}{3}$'

            # B4-Điều chỉnh các phương án sai không trùng đáp án đúng
            # Các phương án sai tạo bằng cách random hoặc các giá trị gần đúng
            sai = ['$\\frac{\\sqrt{2}}{2}$', '$\\frac{\\sqrt{3}}{2}$', '$\\frac{\\sqrt{6}}{3}$', '$\\frac{1}{2}$', '$\\frac{2}{3}$', '$\\frac{1}{3}$']
            # Đảm bảo không trùng đáp án đúng
            if da in sai:
                sai.remove(da)

            ds_sai = random.sample(sai, 3)

            # Các đáp án trắc nghiệm
            list_1 = ['\\True ' + da, ds_sai[0], ds_sai[1], ds_sai[2]]
            random.shuffle(list_1)

            # Nội dung lời giải
            loigiai=('''\\begin{center}
            	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\\draw [line width=1]    (58.86,142.24) -- (163.99,142.24) ;
            		\\draw [line width=1]    (58.86,142.24) -- (59.56,226.02) ;
            		\\draw [line width=1]    (59.56,226.02) -- (164.7,226.02) ;
            		\\draw [line width=1]    (163.99,142.24) -- (164.7,226.02) ;
            		\\draw [line width=1]    (105.21,97.65) -- (210.34,97.65) ;
            		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (105.21,97.65) -- (105.91,181.43) ;
            		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (105.91,181.43) -- (211.05,181.43) ;
            		\\draw [line width=1]    (210.34,97.65) -- (211.05,181.43) ;
            		\\draw [line width=1]    (58.86,142.24) -- (105.21,97.65) ;
            		\\draw [line width=1]    (163.99,142.24) -- (210.34,97.65) ;
            		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (59.56,226.02) -- (105.91,181.43) ;
            		\\draw [line width=1]    (164.7,226.02) -- (211.05,181.43) ;
            		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (163.99,142.24) -- (105.91,181.43) ;
            		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (105.91,181.43) -- (164.7,226.02) ;
            		\\draw (84,167.67) node [anchor=north west][inner sep=0.75pt]    {$A$};
            		\\draw (213.33,158.33) node [anchor=north west][inner sep=0.75pt]    {$D$};
            		\\draw (164.7,226.02) node [anchor=north west][inner sep=0.75pt]    {$C$};
            		\\draw (39.33,209) node [anchor=north west][inner sep=0.75pt]    {$B$};
            		\\draw (80,77.67) node [anchor=north west][inner sep=0.75pt]    {$A\'$};
            		\\draw (210,75.67) node [anchor=north west][inner sep=0.75pt]    {$D\'$};
            		\\draw (150,119.67) node [anchor=north west][inner sep=0.75pt]    {$C\'$};
            		\\draw (40.67,121) node [anchor=north west][inner sep=0.75pt]    {$B\'$};
            	\\end{tikzpicture}
            \\end{center} Gọi cạnh của hình lập phương là $a = %s$. \\\\
                      Ta có $CC' \\perp (ABCD)$ nên hình chiếu vuông góc của $AC'$ lên mặt phẳng $(ABCD)$ là $AC$. \\\\
                      Do đó góc giữa đường thẳng $AC'$ và mặt phẳng $(ABCD)$ là góc $\\widehat{C'AC}$. \\\\
                      Xét tam giác $ACC'$ vuông tại $C$, ta có: \\\\
                      $\\sin \\widehat{C'AC} = \\frac{CC'}{AC'} = \\frac{a}{a\\sqrt{3}} = \\frac{1}{\\sqrt{3}} = \\frac{\\sqrt{3}}{3}$. \\\\
                      Vậy giá trị cần tìm là $\\frac{\\sqrt{3}}{3}$.'''
                     %(latex(a)))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[0])+'}\n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

