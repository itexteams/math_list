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


def bt_dang3_p4_b2_c2_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':

                # Nội dung câu hỏi
                noidungcauhoi = ('''\\immini{Cho hình chóp $S.ABC$. Các điểm $M, N, P$ tương ứng là trung điểm của $SA, SB, SC$. Đường thẳng qua $S$ vuông góc với mặt phẳng $(ABC)$ và cắt mặt phẳng đó tại $H$. Chứng minh rằng $SH \\perp (MNP)$.
                                }{
                    \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
                    \\clip(-1.0005300759814137,-2.521779911742773) rectangle (5.560034034703034,4.648164659815519);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,0.)-- (5.,0.);
                    \\draw [line width=1.pt] (5.,0.)-- (3.,-2.);
                    \\draw [line width=1.pt] (3.,-2.)-- (0.,0.);
                    \\draw [line width=1.pt] (0.,0.)-- (2.,4.);
                    \\draw [line width=1.pt] (2.,4.)-- (3.,-2.);
                    \\draw [line width=1.pt] (2.,4.)-- (5.,0.);
                    \\draw [line width=1.pt] (1.,2.)-- (2.504825141577994,0.9710491505320347);
                    \\draw [line width=1.pt] (2.504825141577994,0.9710491505320347)-- (3.5197135630713516,1.9737152492381975);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (3.5197135630713516,1.9737152492381975)-- (1.,2.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,4.)-- (2.007475603225685,-0.6677074456797787);
                    \\draw (1.8129924774148811,4.661130201536239) node[anchor=north west] {$S$};
                    \\draw (-0.5,0.3306392668156796) node[anchor=north west] {$A$};
                    \\draw (2.8502358150725016,-1.8605372839860406) node[anchor=north west] {$B$};
                    \\draw (5.067343449315665,0.36953589197784037) node[anchor=north west] {$C$};
                    \\draw (0.4,2.4569881090137984) node[anchor=north west] {$M$};
                    \\draw (2.577959438937376,1.1993305621039356) node[anchor=north west] {$N$};
                    \\draw (3.563340609712115,2.444022567293078) node[anchor=north west] {$P$};
                    \\draw (2.020441144946405,-0.36949998610321316) node[anchor=north west] {$H$};
                    \\end{tikzpicture} }  '''
                                %(
                                ))

                # Nội dung lời giải
                loigiai=('''Do $MN // AB, MP // AC$ nên $(MNP) // (ABC)$. \\\\
                        Mặt khác, $SH \\perp (ABC)$. Do đó $SH \\perp (MNP)$.'''
                        %(
                        ))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content        

