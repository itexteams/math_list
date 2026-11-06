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


def bt_dang4_p3_b5_c2_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                a=randint(5,19)
                h1=Rational(a,2)  
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                # Câu hỏi
                noidungcauhoi = ('''Cho hình lăng trụ $ABC.A'B'C'$ có tất cả các cạnh đều bằng $%s$. Góc tạo bởi cạnh bên và mặt phẳng đáy bằng $30^\\circ$. Hình chiếu $H$ của $A$ trên mặt phẳng $(A'B'C')$ là trung điểm của $B'C'$. Khoảng cách giữa hai mặt phẳng đáy của lăng trụ $ABC.A'B'C'$ bằng bao nhiêu? (làm tròn kết quả đến hàng đơn vị).'''
                                %(latex(a)
                                ))

                # Nội dung lời giải
                loigiai=('''\\begin{center}
                \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
                    \\clip(-0.970574737813389,-1.569525714848289) rectangle (5.989942761197689,4.6583057316353);
                    \\draw [line width=1.pt ,dash pattern=on 2pt off 2pt] (0.,0.)-- (4.,0.);
                    \\draw [line width=1.pt ] (4.,0.)-- (2.,-1.);
                    \\draw [line width=1.pt ] (2.,-1.)-- (0.,0.);
                    \\draw [line width=1.pt ] (0.,0.)-- (1.,4.);
                    \\draw [line width=1.pt ] (1.,4.)-- (5.,4.);
                    \\draw [line width=1.pt ] (1.,4.)-- (3.,3.);
                    \\draw [line width=1.pt ] (3.,3.)-- (5.,4.);
                    \\draw [line width=1.pt ] (5.,4.)-- (4.,0.);
                    \\draw [line width=1.pt ] (3.,3.)-- (2.,-1.);
                    \\draw [line width=1.pt ,dash pattern=on 2pt off 2pt] (1.,4.)-- (4.,0.);
                    \\draw [line width=1.pt ,dash pattern=on 2pt off 2pt] (0.,0.)-- (3.,-0.5);
                    \\draw [line width=1.pt ,dash pattern=on 2pt off 2pt] (3.,-0.5)-- (1.,4.);
                    \\draw (0.5490704081695363,4.6583057316353) node[anchor=north west] {$A$};
                    \\draw (3.0727668113197515,3.125092325420386) node[anchor=north west] {$B$};
                    \\draw (5.080869325654332,4.6583057316353) node[anchor=north west] {$C$};
                    \\draw (-0.5499586706216864,0.1536433346144906) node[anchor=north west] {$A'$};
                    \\draw (1.7702138290486729,-0.945385744176731) node[anchor=north west] {$B'$};
                    \\draw (4.144659369646994,0.2757576767024041) node[anchor=north west] {$C'$};
                \\end{tikzpicture}
            \\end{center}
                        Góc tạo bởi cạnh bên và mặt phẳng đáy bằng $30^\\circ$ nên $\\widehat{AA'H} = 30^\\circ$.
                        Khoảng cách giữa hai mặt phẳng đáy của lăng trụ $ABC.A'B'C'$ bằng
                        $AH = AA' \\cdot \\sin \\widehat{AA'H} = AA' \\cdot \\sin 30^\\circ = %s$.'''
                        %(latex(Rational(a,2))
                        ))

            #Đáp án
            dapan=' \\shortans[0]{$%s$} '%(latex(kq))
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

