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


def bt_dang51_p3_b3_c2_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                k=randint(1,9)
                a=2*k
                b=3*k
                h1=Rational(a*b,4)   
                number = Decimal(float(h1))  # Số cần làm tròn
                kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy là hình thang vuông tại $A$ và $D$, $AB = 2AD = 2CD = %s$. Biết $SA \\perp (ABCD)$, $SA = %s$. Diện tích hình chiếu vuông góc của tam giác $SBC$ lên mặt phẳng $(SAB)$ là bao nhiêu? (làm tròn kết quả đến hàng phần chục).'''
                                %(latex(a),latex(b)
                                ))

                # Nội dung lời giải
                loigiai = ('''\\begin{center}
                \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
                    \\clip(-1.014534589920362,-0.9609428719785006) rectangle (5.862077565748368,4.887247376480839);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,0.)-- (1.,1.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (1.,1.)-- (5.,1.);
                    \\draw [line width=1.pt] (0.,0.)-- (2.,0.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,0.)-- (3.,1.);
                    \\draw [line width=1.pt] (2.,0.)-- (5.,1.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (1.,1.)-- (1.,4.);
                    \\draw [line width=1.pt] (1.,4.)-- (0.,0.);
                    \\draw [line width=1.pt] (1.,4.)-- (2.,0.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (1.,4.)-- (3.,1.);
                    \\draw [line width=1.pt] (1.,4.)-- (5.,1.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (1.,1.)-- (2.,0.);
                    \\draw (0.7967159332245269,4.6) node[anchor=north west] {$S$};
                    \\draw (4.9,1.5) node[anchor=north west] {$B$};
                    \\draw (1.932584905366237,0.12887735804935535) node[anchor=north west] {$C$};
                    \\draw (-0.5540471687818309,0.17492610016320842) node[anchor=north west] {$D$};
                    \\draw (3.0377547160987115,1.5) node[anchor=north west] {$I$};
                    \\draw (0.4897243191321729,1.5) node[anchor=north west] {$A$};
                \\end{tikzpicture}
            \\end{center}
            Gọi $I$ là trung điểm $AB$.\\\\
            Dễ dàng chứng minh $AICD$ là hình vuông $\\Rightarrow CI = \\frac{1}{2}AB \\Rightarrow \\triangle ABC$ vuông tại $C$. \\\\
            Ta có: \\\\
            $\\begin{cases}
                    CI \\perp AB \\\\
                    CI \\perp SA
                \\end{cases} \\Rightarrow CI \\perp (SAB)$. \\\\
            Hình chiếu của $\\triangle SBC$ trên $(SAB)$ là $\\triangle SIB$. \\\\
            $S_{\\triangle SIB} = \\frac{1}{2} S_{\\triangle SAB} = \\frac{1}{2} \\cdot \\frac{1}{2} \\cdot SA \\cdot AB = \\frac{1}{4} \\cdot %s \\cdot %s = %s=%s$.'''
                        %(latex(b),latex(a),latex(h1),latex(kq)
                        ))

                #Đáp án
                dapan=' \\shortans[0]{$%s$} '%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content     

