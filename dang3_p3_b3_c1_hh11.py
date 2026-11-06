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


def bt_dang3_p3_b3_c1_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                a=randint(2,50)
                h1=1
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho tứ diện $ABCD$ và điểm $M$ là trung điểm của $AB$. Gọi $(\\alpha)$ là mặt phẳng qua $M$, song song với hai đường thẳng $BC$ và $AD$. Gọi $N, P, Q$ lần lượt là giao điểm của mặt phẳng $(\\alpha)$ với các cạnh $AC, CD$ và $DB$. Biết $AD = kBC$ thì $MQ = %sPQ$. Giá trị của $k$ bằng bao nhiêu? ($k \\in \\mathbb{R}, k > 0$).  \n'
                                %(latex(a)
                                ))

                # Nội dung lời giải
                loigiai = (

                            '\\begin{center}   \n'
                        '\\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]   \n'
                            '\\clip(-0.6299564356716434,-2.4943387257828853) rectangle (6.097175135104381,3.7186171835325283);  \n'
                            '\\draw (0.,0.)-- (3.,-2.);  \n'
                            '\\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (5.,0.);  \n'
                            '\\draw (5.,0.)-- (3.,-2.);  \n'
                            '\\draw (0.,0.)-- (3.,3.);  \n'
                            '\\draw (3.,3.)-- (3.,-2.);  \n'
                            '\\draw (3.,3.)-- (5.,0.);  \n'
                            '\\draw (1.5,1.5)-- (3.,0.5);  \n'
                            '\\draw (3.,0.5)-- (4.,-1.);  \n'
                            '\\draw [dash pattern=on 2pt off 2pt] (1.5,1.5)-- (2.5,0.);  \n'
                            '\\draw [dash pattern=on 2pt off 2pt] (2.5,0.)-- (4.,-1.);  \n'
                            '\\draw (2.7,3.5) node[anchor=north west] {A};  \n'
                            '\\draw (2.7,-2) node[anchor=north west] {B};  \n'
                            '\\draw (-0.56,0.3) node[anchor=north west] {C};  \n'
                            '\\draw (4.97,0.3) node[anchor=north west] {D};  \n'
                            '\\draw (3.1192410958118093,0.8) node[anchor=north west] {M};  \n'
                            '\\draw (1,1.9) node[anchor=north west] {N};  \n'
                            '\\draw (2.32,0.6) node[anchor=north west] {P};  \n'
                            '\\draw (4.051184482209124,-0.9) node[anchor=north west] {Q};  \n'
                        '\\end{tikzpicture}   \n'
                    '\\end{center}   \n'

                        'Ta có $\\heva{& (MNPQ) \\cap (ABC) = MN \\\\& BC // (MNPQ)} \\Rightarrow MN // BC$. \\\\ \n'
                        '\\hspace*{1cm} $\\heva{& (MNPQ) \\cap (BCD) = PQ \\\\& BC // (MNPQ)} \\Rightarrow BC // PQ$. \\\\ \n'
                        'Vậy $MN // PQ$. \\\\ \n'
                        'Chứng minh tương tự ta có $NP // MQ$. \\\\ \n'
                        'Suy ra MNPQ là hình bình hành. \\\\ \n'
                        'Để $MQ = %s PQ \\Leftrightarrow \\frac{1}{2}AD = %s \\cdot \\frac{1}{2}BC \\Leftrightarrow AD = %s BC$. \\\\ \n'
                        'Vậy $k=%s$.'
                        %(latex(a),latex(a), latex(a), latex(a)
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(a))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content             

