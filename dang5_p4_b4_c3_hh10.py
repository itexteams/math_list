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


def bt_dang5_p4_b4_c3_hh10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                # Khai báo biến
                a=randint(3,15)
                b=randint(2,14)
                while a<=b:
                    a=randint(3,15)
                    b=randint(2,14)
                k=Rational(2,a*b)
                y02=Rational(b**2,2)
                y0=sqrt(y02)
                x02=Rational(a**2*y02,b**2)
                x0=sqrt(x02)

                # Câu hỏi
                noidungcauhoi = ('Cho elip $(E): \\dfrac{x^2}{%s}+\\dfrac{y^2}{%s}=1$. Tìm tọa độ điểm $A$ và $B$ thuộc $(E)$ có hoành độ dương sao cho tam giác $OAB$ cân tại $O$ và có diện tích lớn nhất.'

                                %(latex(a**2),latex(b**2)))

                # Nội dung lời giải
                loigiai=('Do tam giác $OAB$ cân tại $O$ và hai điểm $A,B$ có hoành độ dương nên $A,B$ đối xứng nhau qua $Ox$.'
                        '''\\begin{center}
                        \\scalebox{0.7}{
                        \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]
                    \\clip(-4.2662587906409275,-2.59171520689146) rectangle (4.602171746331732,2.55);
                    \\fill[line width=1.2pt,fill=black,pattern=north east lines,pattern color=black] (1.0052566588576017,1.6536766283648117) -- (0.,0.) -- (0.9939103225775593,-1.656712691697445) -- cycle;
                    \\draw [rotate around={0.:(0.,0.)}] (0.,0.) ellipse (2.68cm and 1.7839282496782203cm);
                    \\draw [line width=1.2pt] (1.0052566588576017,1.6536766283648117)-- (0.,0.);
                    \\draw [line width=1.2pt] (0.,0.)-- (0.9939103225775593,-1.656712691697445);
                    \\draw [line width=1.2pt] (0.9939103225775593,-1.656712691697445)-- (1.0052566588576017,1.6536766283648117);
                    \\draw [->] (-3.345705328469789,0.) -- (3.681618284160593,0.);
                    \\draw [->] (0.,-2.4101976228013764) -- (0.,2.529673772793044);
                    \\draw (-0.5,0.05325530413547379) node[anchor=north west] {$O$};
                    \\draw (0.9,2.283328480099359) node[anchor=north west] {$A$};
                    \\draw (0.9,-1.6192995778374402) node[anchor=north west] {$B$};
                    \\draw (3.240789865656104,-0.1) node[anchor=north west] {$x$};
                    \\draw (-0.4543895247491705,2.6333981065588064) node[anchor=north west] {$y$};
                    \\draw (1,0.48111818091924247) node[anchor=north west] {$H$};
                \\end{tikzpicture}}
                        \\end{center}'''
                        'Giả sử $A(x;y)$ với $x>0$, suy ra $B(x;-y)$. Gọi $H$ là hình chiếu của $O$ trên $AB$.\\\\ \n'
                        'Khi đó $S_{\\Delta OAB}=\\dfrac{1}{2}AB\\cdot OH=\\dfrac{1}{2}|2y|x=x|y|$.\\\\ \n'
                        'Theo bất đẳng thức AM-GM: $1=\\dfrac{x^2}{%s}+\\dfrac{y^2}{%s}\\ge 2\\sqrt{\\dfrac{x^2}{%s}\\cdot\\dfrac{y^2}{%s}}=%s x|y|$,  $(x>0)$.\\\\ \n'
                        'Do đó $S_{\\Delta OAB}=x|y|\\le %s$. Dấu "$=$" xảy ra khi và chỉ khi $\\dfrac{x^2}{%s}=\\dfrac{y^2}{%s}$.\\\\ \n'
                        'Thay vào  $(E): \\dfrac{x^2}{%s}+\\dfrac{y^2}{%s}=1$, ta được  $(E): \\dfrac{y^2}{%s}+\\dfrac{y^2}{%s}=1 \\Leftrightarrow y^2=%s \\Leftrightarrow y=\\pm %s$.\\\\ \n'
                        'Suy ra $x^2=%s \\Rightarrow x=%s $.\\\\ \n'
                        'Vậy $A\\left(%s;%s\\right),B\\left(%s;%s\\right)$ hoặc $A\\left(%s;%s\\right),B\\left(%s;%s\\right)$.'

                        %(latex(a**2),latex(b**2),latex(a**2),latex(b**2),latex(k),
                        latex(1/k),latex(a**2),latex(b**2),
                        latex(a**2),latex(b**2),latex(b**2),latex(b**2),latex(y02),latex(y0),
                        latex(x02),latex(x0),
                        latex(x0),latex(y0),latex(x0),latex(-y0),latex(x0),latex(-y0),latex(x0),latex(y0),


                        ))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('- +','-').replace('+ -', '-').replace('- -', '+')
            return content 

