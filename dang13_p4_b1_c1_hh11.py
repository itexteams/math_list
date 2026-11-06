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


def bt_dang13_p4_b1_c1_hh11(self):
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
                noidungcauhoi = (r'''Cho tứ diện $ABCD$. Gọi $M, N$ lần lượt là trung điểm của $AB$ và $CD$. 
                                 Mặt phẳng $(\alpha)$ qua $MN$ cắt $AD, BC$ lần lượt tại $P$ và $Q$.
                                 Biết $MP$ cắt $NQ$ tại $I$. Chứng minh rằng ba điểm $I,\text{ }B,\text{ }D$ thẳng hàng.'''
                )

                # Nội dung lời giải
                loigiai = ('''\\begin{center}
            \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,scale=0.7]
            	\\clip(-1.68,-2.86) rectangle (10.64,5.88);
            	\\draw (2.,5.)-- (0.,0.);
            	\\draw (0.,0.)-- (2.,-2.);
            	\\draw (2.,5.)-- (2.,-2.);
            	\\draw [dash pattern=on 1pt off 1pt] (1.,2.5)-- (9.,0.);
            	\\draw [dash pattern=on 1pt off 1pt] (1.3846153846153846,-1.3846153846153846)-- (3.5,-1.);
            	\\draw (3.5,-1.)-- (9.,0.);
            	\\draw (4.076923076923077,1.5384615384615385)-- (3.5,-1.);
            	\\draw [dash pattern=on 1pt off 1pt] (3.5,-1.)-- (1.,2.5);
            	\\draw (2.,-2.)-- (3.5,-1.);
            	\\draw [dash pattern=on 1pt off 1pt] (3.5,-1.)-- (5.,0.);
            	\\draw (2.,5.)-- (4.076923076923077,1.5384615384615385);
            	\\draw [dash pattern=on 1pt off 1pt] (4.076923076923077,1.5384615384615385)-- (5.,0.);
            	\\draw [dash pattern=on 1pt off 1pt] (0.,0.)-- (9.,0.);
            	\\draw (4.076923076923077,1.5384615384615385)-- (9.,0.);
            	\\draw (1.74,5.86) node[anchor=north west] {$A$};
            	\\draw (-0.86,0.58) node[anchor=north west] {$B$};
            	\\draw (1.38,-1.9) node[anchor=north west] {$C$};
            	\\draw (5.,0.7) node[anchor=north west] {$D$};
            	\\draw (9,0.6) node[anchor=north west] {$I$};
            	\\draw (4.2,2.3) node[anchor=north west] {$P$};
            	\\draw (0.2,3.28) node[anchor=north west] {$M$};
            	\\draw (3.2,-1) node[anchor=north west] {$N$};
            \\end{tikzpicture}
                           \\end{center}'''
                    r''' Ta có: $I \in MP$. Mà $MP \subset (ABD)$, suy ra $I \in (ABD)$. \\
                Ta có: $I \in NQ$. Mà $NQ \subset (BCD)$, suy ra $I \in (BCD)$. \\
                Vì $I$ thuộc cả hai mặt phẳng $(ABD)$ và $(BCD)$, nên $I$ phải thuộc giao tuyến của chúng. \\
                Mặt khác, $(ABD) \cap (BCD) = BD$. \\
                Vậy $I \in BD$, hay ba điểm $I, B, D$ thẳng hàng.''')

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content 

