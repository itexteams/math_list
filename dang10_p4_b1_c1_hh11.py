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


def bt_dang10_p4_b1_c1_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                a=randint(2,9)


                # Nội dung câu hỏi
                noidungcauhoi = ('Cho tứ diện $ABCD$. Gọi $M$, $N$ lần lượt là trung điểm của $AC$ và $AD$. $O$ là một điểm bên trong $\\triangle BCD$. Tìm giao điểm. \\\\'
                                 'a) $MN$ và $\\left(ABO\\right)$. \\\\'
                                 'b) $AO$ và $\\left(BMN\\right)$. \\\\'
                                 %(
                                 ))

                # Nội dung lời giải
                loigiai = (    '''\\begin{center}
            	\\begin{tikzpicture}
            		\\coordinate (A) at (2,3); \\node[above] at (A) {$A$};
            		\\coordinate (B) at (0,0); \\node[left] at (B) {$B$};
            		\\coordinate (C) at (1,-1); \\node[below] at (C) {$C$};
            		\\coordinate (D) at (4,0); \\node[right] at (D) {$D$};
            		\\coordinate (I) at (2.5,-0.5); \\node[below] at (I) {$I$};
            		\\coordinate (O) at (2,-0.5); \\node[left] at (O) {$O$};
            		\\coordinate (M) at (1.68,1.73); \\node[left] at (M) {$M$};
            		\\coordinate (N) at (3.35,0.97); \\node[right] at (N) {$N$};
            		\\coordinate (J) at (2.22,1.47); \\node[above right] at (J) {$J$};
            		\\coordinate (K) at (1.99,1.32); \\node[below] at (K) {$K$};
            		\\draw[line width=1pt] (M)--(N);
            		\\draw[line width=1pt] (A)--(B);
            		\\draw[line width=1pt] (A)--(I);
            		\\draw[line width=1pt] (A)--(C);
            		\\draw[line width=1pt] (A)--(D);
            		\\draw[line width=1pt] (B)--(C);
            		\\draw[line width=1pt,dashed] (B)--(D);
            		\\draw[line width=1pt,dashed] (B)--(I);
            		\\draw[line width=1pt,dashed] (B)--(J);
            		\\draw[line width=1pt,dashed] (A)--(O);
            		\\draw[line width=1pt] (D)--(C);
            	\\end{tikzpicture}
            \\end{center}
            \\begin{enumEX}[a)]{1} 
                                \\item  Trong $\\left(BCD\\right)$ kẻ $BO$ giao $CD$ tại $I$.\\\\
                                    Trong $\\left(ACD\\right)$ kẻ $MN$ giao $AI$ tại $J$ $\\Rightarrow J$ là giao điểm của $MN$ và $\\left(ABO\\right)$.
                                \\item  Trong $\\left(ABI\\right)$: $AO$ giao $BJ$ tại $K$ $\\Rightarrow K$ là giao điểm của $AO$ và $\\left(BMN\\right)$.
                                \\end{enumEX}'''

                           %(
                           ))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content 

