
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


def bt_dang25_p1_b5_c1_hh11(self):
    # Khai báo biến
    lisdang=['1']
    dang=random.choice(lisdang)
    if dang=='1':
        hinh_ve = '''\\begin{center}
    \\begin{tikzpicture}[scale=0.8, line width=1pt]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (3,-1);
    \\coordinate (D) at (2,1);
    \\coordinate (C) at (5,0);
    \\coordinate (A') at (0,3);
    \\coordinate (B') at (3,2);
    \\coordinate (D') at (2,4);
    \\coordinate (C') at (5,3);
    \\coordinate (I) at (8,-1);
    \\draw (A) -- (B) -- (C);
    \\draw (A') -- (B') -- (C') -- (D') -- cycle;
    \\draw (A) -- (A');
    \\draw (B) -- (B');
    \\draw (C) -- (C');
    \\draw (C) -- (I) -- (B);
    \\draw (A') -- (B);
    \\draw (C') -- (I);
    \\draw[dashed] (A) -- (D);
    \\draw[dashed] (D) -- (D');
    \\draw[dashed] (C) -- (D');
    \\draw[dashed] (D) -- (I);
    \\draw[dashed] (A') -- (D');
    \\node[below left] at (A) {$A$};
    \\node[below] at (B) {$B$};
    \\node[above left] at (D) {$D$};
    \\node[above right] at (C) {$C$};
    \\node[left] at (A') {$A'$};
    \\node[above] at (B') {$B'$};
    \\node[above left] at (D') {$D'$};
    \\node[above right] at (C') {$C'$};
    \\node[right] at (I) {$I$};
    \\fill (A) circle (1.5pt); \\fill (B) circle (1.5pt); \\fill (C) circle (1.5pt); \\fill (D) circle (1.5pt);
    \\fill (A') circle (1.5pt); \\fill (B') circle (1.5pt); \\fill (C') circle (1.5pt); \\fill (D') circle (1.5pt);
    \\fill (I) circle (1.5pt);
    \\end{tikzpicture}
    \\end{center}'''
        noidungcauhoi = "Cho hình hộp $ABCD.A'B'C'D'$. Hình biểu diễn của $\\Delta A'C'D'$ qua phép chiếu song song lên mặt phẳng $(ABCD)$ theo phương $A'B$ là"
        da_d = '\\True Một tam giác $BCI$, với $I$ là điểm sao cho $C$ là trung điểm của $DI$'
        da_s1 = 'Một tam giác $ABC$'
        da_s2 = 'Một tam giác $ACD$'
        da_s3 = 'Một tam giác $DCM$, với $M$ là điểm sao cho $C$ là trung điểm của $BM$'
        list_1 = [da_d, da_s1, da_s2, da_s3]
        random.shuffle(list_1)
        loigiai = "Gọi $f$ là phép chiếu song song lên mặt phẳng $(ABCD)$ theo phương $A'B$. Khi đó, $f$ biến:\\\\ + điểm $A'$ thành điểm $B$,\\\\ + điểm $D'$ thành điểm $C$\\\\ + điểm $C'$ thành điểm $I$, với $I$ là điểm sao cho $C$ là trung điểm của $DI$.\\\\ Vì vậy, ảnh của tam giác $A'C'D'$ qua phép chiếu song song lên mặt phẳng $(ABCD)$ theo phương $A'B$ là tam giác $BCI$." + hinh_ve
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
        '\\choice \n'
        '{'+str(list_1[1])+'}\n'
        '{'+str(list_1[2])+'}\n'
        '{'+str(list_1[3])+'}\n'
        '{'+str(list_1[0])+'}\n'
        '\\loigiai{'+str(loigiai)+'}\n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content
