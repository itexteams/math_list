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


def bt_dang15_p4_b1_c1_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':

                # Các đối tượng hình học (chỉ dùng để điền vào câu hỏi)
                diem_I = r'I \in SA, SA=3IA'
                diem_J = r'J \in SC'
                diem_M = r'M \text{ là trung điểm của } SB'
                mp_IJM = r'(IJM)'
                dt_AB = r'AB'

                # Kết quả cần tìm
                kq_diem = r'E'

                # Câu hỏi
                noidungcauhoi = (r'''Cho mặt phẳng $(P)$ và ba điểm $A, B, C$ không thẳng hàng và ở ngoài $(P)$. 
                                 Giả sử các đường thẳng $BC, CA, AB$ lần lượt cắt $(P)$ tại các điểm $D, E, F$. 
                                 Chứng minh ba điểm $D, E, F$ thẳng hàng.'''
                )

                # Nội dung lời giải
                loigiai = ('''\\begin{center}
                           \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,scale=0.4]
            	\\clip(-2.665994423353169,-0.6924852345891651) rectangle (17.176184415785354,12.685104265244355);
            	\\draw (0.,0.)-- (10.,0.);
            	\\draw (10.,0.)-- (14.,4.);
            	\\draw (2.,0.)-- (10.,4.);
            	\\draw (10.,4.)-- (10.,12.);
            	\\draw (10.,12.)-- (2.,8.);
            	\\draw (2.,8.)-- (2.,0.);
            	\\draw (0.,0.)-- (2.,2.);
            	\\draw [dash pattern=on 2pt off 2pt] (2.,2.)-- (4.,4.);
            	\\draw [dash pattern=on 2pt off 2pt] (4.,4.)-- (10.,4.);
            	\\draw (10.,4.)-- (14.,4.);
            	\\draw (5.44276792710457,9.060450127021307)-- (3.6476006640977627,0.8238003320488813);
            	\\draw (5.44276792710457,9.060450127021307)-- (7.047260124786055,2.523630062393028);
            	\\draw (4.8075192637046555,6.145779789068752)-- (8.67138753995507,3.3356937699775355);
            	\\draw (3.6,7.1173365683862695) node[anchor=north west] {$B$};
            	\\draw (5.517503063975148,10.29357988538585) node[anchor=north west] {$C$};
            	\\draw (6.3,6.519455473421643) node[anchor=north west] {$A$};
            	\\draw (12,4.26) node[anchor=north west] {$(P$};
            	\\draw (3.7238597790812706,1.4) node[anchor=north west] {$D$};
            	\\draw (6.750632822339689,2.9321689036338836)node[anchor=north west] {$E$};
            	\\draw (8.693746380974725,3.9037256829514018) node[anchor=north west] {$F$};
            \\end{tikzpicture}
                           \\end{center}'''
                    r'''Vì $A, B, C$ không thẳng hàng nên chúng xác định một mặt phẳng duy nhất là $(ABC)$. \\
                Ta có: \\
                $D = BC \cap (P)$. Vì $BC \subset (ABC)$, suy ra $D \in (ABC)$ và $D \in (P)$. $\implies D \in (ABC) \cap (P)$. \\
                $E = CA \cap (P)$. Vì $CA \subset (ABC)$, suy ra $E \in (ABC)$ và $E \in (P)$. $\implies E \in (ABC) \cap (P)$. \\
                $F = AB \cap (P)$. Vì $AB \subset (ABC)$, suy ra $F \in (ABC)$ và $F \in (P)$. $\implies F \in (ABC) \cap (P)$. \\
                Khi đó ba điểm $D, E, F$ đều thuộc giao tuyến của hai mặt phẳng $(ABC)$ và $(P)$. Do giao tuyến của hai mặt phẳng là một đường thẳng nên $D, E, F$ thẳng hàng.''')

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content 

