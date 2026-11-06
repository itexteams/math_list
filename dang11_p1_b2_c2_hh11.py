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


def bt_dang11_p1_b2_c2_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':

                du = ['$IK \\perp (SBD)$',
                    ]
                da= random.choice(du)
                s = ['$IK \\perp (SAB)$',
                    '$IK \\perp (SAC)$',
                    '$IK \\perp (SAD)$',
                    '$IK \\perp (SBC)$',
                    '$IK \\perp (SCD)$',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''\\immini{Cho hình chóp $S.ABCD$ có đáy là hình thoi $ABCD$ tâm $O$ và có $SA = SC$, $SB = SD$. Cho $I$, $K$ lần lượt là trung điểm của các cạnh $AB$, $BC$. Khẳng định nào sau đây đúng?
                                }{
            \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
                    \\clip(-0.6796534474573865,-0.7256784644126393) rectangle (6.601762809036017,4.770207892662377);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,0.)-- (2.,1.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,1.)-- (6.,1.);
                    \\draw [line width=1.pt] (6.,1.)-- (4.,0.);
                    \\draw [line width=1.pt] (4.,0.)-- (0.,0.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,1.)-- (4.,0.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,0.)-- (6.,1.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (3.,0.5)-- (3.,4.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (3.,4.)-- (2.,1.);
                    \\draw [line width=1.pt] (3.,4.)-- (0.,0.);
                    \\draw [line width=1.pt] (3.,4.)-- (4.,0.);
                    \\draw [line width=1.pt] (3.,4.)-- (6.,1.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (1.131355078891254,0.565677539445627)-- (1.8656764091603073,0.);
                    \\draw (2.840753020899424,4.65623789908248) node[anchor=north west] {$S$};
                    \\draw (1.5744197589005713,1.5410580745653053) node[anchor=north west] {$A$};
                    \\draw (-0.54,0.236734814706488) node[anchor=north west] {$B$};
                    \\draw (4.043769619798334,0.13542815374657985) node[anchor=north west] {$C$};
                    \\draw (6.107892836856464,1.3004547547855234) node[anchor=north west] {$D$};
                    \\draw (2.7394463599395156,0.5) node[anchor=north west] {$O$};
                    \\draw (0.8652731321812137,1.1231680981056842) node[anchor=north west] {$I$};
                    \\draw (1.5997464241405484,0.08477482326662579) node[anchor=north west] {$K$};
            \\end{tikzpicture}}  '''
                                %(
                                ))
                # Các đáp án
                da_d = ('\\True ' +str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 
                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d,da_s1,da_s2,da_s3]
                random.shuffle(list_1)
                # Nội dung lời giải
                loigiai=('''Ta có $ABCD$ là hình thoi, suy ra $AC$, $BD$ vuông góc với nhau và có cùng trung điểm $O$. \\\\
                            Tam giác $SAC$ cân tại $S$ nên $SO \\perp AC$. Tương tự, ta có $SO \\perp BD$. \\\\
                            Do $SO$ vuông góc với hai đường thẳng cắt nhau $AC$ và $BD$ trong $(ABCD)$, suy ra $SO \\perp (ABCD)$. \\\\
                            Ta có $IK // AC$ và $AC \\perp BD$, do đó $IK \\perp BD$. \\\\
                            Ta có $SO \\perp (ABCD)$, do đó $SO \\perp IK$. \\\\
                            Từ $IK \\perp BD$ và $IK \\perp SO$ suy ra $IK \\perp (SBD)$. '''
                        %(
                        ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

