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


def bt_dang4_p4_b1_c2_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                lis=[1,2,3,4,5,6,7,8,9]
                k=random.choice(lis)
                h=randint(2,9)
                ab=h*k
                cd=ab
                lis1=[1.6,1.7,1.8,1.8]
                i=random.choice(lis1)
                mn=i*k
                mp=Rational(ab,2)
                np=mp
                gtri=(mp**2+np**2-mn**2)/(2*mp*np)

                goc1=acos(gtri)
                gocz=goc1*180/pi

                h1=gocz
                number = Decimal(float(h1))  # Số cần làm tròn
                goc = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Nội dung câu hỏi
                noidungcauhoi = ('''                     
                                Cho tứ diện $ABCD$, gọi $M$, $N$ là trung điểm của $BC$, $AD$zz Biết $AB=CD=%s$, $MN=%s$zz Tính góc giữa hai đường thẳng $AB$ và $CD$zz
                                '''
                                %(latex(ab),latex(mn)
                                ))

                # Nội dung lời giải
                loigiai=('''\\begin{center}
                \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1zz0cm,y=1zz0cm]
                    \\clip(-0zz932855898706233,-2zz4437196590214043) rectangle (5zz677592555992239,3zz6568064043609168);
                    \\draw [line width=1zzpt,dash pattern=on 2pt off 2pt] (0zz,0zz)-- (5zz,0zz);
                    \\draw [line width=1zzpt] (0zz,0zz)-- (2zz,-2zz);
                    \\draw [line width=1zzpt] (2zz,-2zz)-- (5zz,0zz);
                    \\draw [line width=1zzpt] (0zz,0zz)-- (1zz5,3zz);
                    \\draw [line width=1zzpt] (1zz5,3zz)-- (5zz,0zz);
                    \\draw [line width=1zzpt] (1zz5,3zz)-- (2zz,-2zz);
                    \\draw [line width=1zzpt] (1zz75,0zz5)-- (3zz25,1zz5);
                    \\draw [line width=1zzpt] (1zz75,0zz5)-- (1zz,-1zz);
                    \\draw [line width=1zzpt,dash pattern=on 2pt off 2pt] (1zz,-1zz)-- (3zz25,1zz5);
                    \\draw (1zz2,3zz5) node[anchor=north west] {$A$};
                    \\draw (-0zz6,0zz25423335685132414) node[anchor=north west] {$B$};
                    \\draw (1zz8578102792239772,-1zz9245259514995048) node[anchor=north west] {$C$};
                    \\draw (5zz0656856864128565,0zz29131862167431694) node[anchor=north west] {$D$};
                    \\draw (0zz4,-0zz904681168867202) node[anchor=north west] {$M$};
                    \\draw (3zz276321658703453,1zz9508842225032463) node[anchor=north west] {$N$};
                    \\draw (1zz2,0zz8105123291962166) node[anchor=north west] {$P$};
                \\end{tikzpicture}
            \\end{center}
                    Do $AB$ và $CD$ là các cạnh của tứ diện nên chúng chéo nhau, để xác định góc giữa hai đường thẳng $AB$ và $CD$ ta tạo các đường thẳng tương ứng song song với $AB$, $CD$ và chúng cắt nhauzz\\\\
                    Gọi $P$ là trung điểm của $AC$, khi đó $MP//AB$, $NP//CD$zz \\\\ 
                    $\\Rightarrow \\left(AB,CD\\right)=\\left(MP,NP\\right)=\\hoac{ &\\widehat{MPN}\\\\ &180^\\circ-\\widehat{MPN}}$zz\\\\
                    Do $MP$, $NP$ là các đường trung bình nên ta có $MP=NP=%s$zz \\\\
                    Áp dụng định lý hàm số cosin trong $\\triangle MPN$ ta được:\\\\
                    $\\cos \\widehat{MPN}=\\dfrac{M{{P}^2}+N{{P}^2}-M{{N}^2}}{2\\cdot MP \\cdot NP}=\\dfrac{%s+%s-%s}{2\\cdot %s \\cdot %s}=%s$zz\\\\
                    Suy ra $\\widehat{MPN}=%s^\\circ$ $\\Leftrightarrow \\left(MP,NP\\right)=%s^\\circ$zz \\\\
                    Vậy $\\left(AB,CD\\right)=%s^\\circ$zz'''
                        %(latex(mp),
                        latex(mp**2),latex(np**2),latex(mn**2),latex(mp),latex(np),latex(gtri),
                        latex(goc),latex(180-goc),
                        latex(180-goc)
                        ))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('zz', '.')
            return content   

