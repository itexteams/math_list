
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


def bt_dang11_p2_b5_c1_hh11(self):
    noidungcauhoi = ('''Cho hình lăng trụ $ABC.A'B'C'$; $I$ và $I'$ lần lượt là trung điểm của đoạn $AB$ và $A'B'$.''')
    nb_da_1_d = '\\True $AI\' \\parallel IB\'$'
    nb_da_1_s = '$AI\' \\parallel I\'B$'
    list_nb_da_1=[nb_da_1_d,nb_da_1_s]
    nb_da_1=random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]
    loigiai_nb_1 = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A') at (0,0);
    \\coordinate (C') at (1,-1.5);
    \\coordinate (B') at (4,0);
    \\coordinate (A) at (1.5,3);
    \\coordinate (C) at ($(A)+(C')-(A')$);
    \\coordinate (B) at ($(A)+(B')-(A')$);
    \\coordinate (I) at ($(A)!0.5!(B)$);
    \\coordinate (I') at ($(A')!0.5!(B')$);
    \\coordinate (M) at ($(C')+(B')-(I')$);
    \\draw[line width=1pt] (A) -- (C) -- (B) -- cycle;
    \\draw[line width=1pt] (A') -- (C') -- (B');
    \\draw[line width=1pt] (A) -- (A') (B) -- (B') (C) -- (C');
    \\draw[line width=1pt] (C') -- (M) -- (C);
    \\draw[dashed, line width=1pt] (A') -- (B') (A) -- (I') (I) -- (B') (M) -- (I') -- (C) (A) -- (M);
    \\fill (A) circle (1.5pt) node[above] {$A$};
    \\fill (B) circle (1.5pt) node[right] {$B$};
    \\fill (C) circle (1.5pt) node[above] {$C$};
    \\fill (A') circle (1.5pt) node[left] {$A'$};
    \\fill (B') circle (1.5pt) node[right] {$B'$};
    \\fill (C') circle (1.5pt) node[below] {$C'$};
    \\fill (I) circle (1.5pt) node[above] {$I$};
    \\fill (I') circle (1.5pt) node[left] {$I'$};
    \\fill (M) circle (1.5pt) node[below right] {$M$};
    \\end{tikzpicture}
    \\end{center}
    Ta có $\\begin{cases} AI \\parallel B'I' \\\\ AI = B'I' = \\dfrac{AB}{2} \\end{cases} \\Rightarrow AIB'I'$ là hình bình hành, do đó $AI' \\parallel IB'$.''')
    list_nb_2 = [loigiai_nb_1]
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    th_da_1_s = 'Hình chiếu song song của $I$ trên mặt phẳng $(A\'B\'C\')$ phương $A\'I$ là điểm $C\'$'
    th_da_1_d = '\\True Hình chiếu song song của $I$ trên mặt phẳng $(A\'B\'C\')$ phương $A\'I$ là điểm $B\'$'
    list_th_da_1=[th_da_1_d,th_da_1_s]
    th_da_1=random.choice(list_th_da_1)
    list_th_1 = [th_da_1]
    loigiai_th_1 = ('''Vì $AI' \\parallel IB'$ nên hình chiếu song song của $I$ trên $(A'B'C')$ phương $A'I$ là điểm $B'$.''')
    list_th_2 = [loigiai_th_1]
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    vd_da_1_d = '\\True Trong $(A\'B\'C\')$, vẽ hình bình hành $A\'C\'MI\'$. Suy ra $ACMI\'$ là hình bình hành'
    vd_da_1_s = 'Trong $(A\'B\'C\')$, vẽ hình bình hành $A\'C\'MI\'$. Suy ra $ACMI\'$ là hình thang'
    list_vd_da_1=[vd_da_1_d,vd_da_1_s]
    vd_da_1=random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]
    loigiai_vd_1 = ('''Trong mặt phẳng $(A'B'C')$, vẽ hình bình hành $A'C'MI'$
    Vì $\\begin{cases} MI' \\parallel A'C', MI' = A'C' \\\\ A'C' \\parallel AC, A'C' = AC \\end{cases} \\Rightarrow MI' \\parallel AC, MI' = AC$.
    Suy ra $ACMI'$ là hình bình hành.''')
    list_vd_2 = [loigiai_vd_1]
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    vdc_da_1_s = '$\\Delta MAA\'$ là hình chiếu song song của $\\Delta CAA\'$ theo phương $AI\'$ trên $(A\'B\'C\')$'
    vdc_da_1_d = '\\True $\\Delta MI\'A\'$ là hình chiếu song song của $\\Delta CAA\'$ theo phương $AI\'$ trên $(A\'B\'C\')$'
    list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
    vdc_da_1=random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]
    loigiai_vdc_1 = ('''Vì $ACMI'$ là hình bình hành nên $AI' \\parallel CM$, mà $M \\in (A'B'C')$
    Nên $M$ chính là hình chiếu song song của $C$ theo phương $AI'$ trên $(A'B'C')$.
    $I'$ chính là hình chiếu song song của $A$ theo phương $AI'$ trên mặt phẳng $(A'B'C')$.
    Vậy hình chiếu song song của $\\Delta CAA'$ theo phương $AI'$ trên $(A'B'C')$ là $\\Delta MI'A'$.''')
    list_vdc_2 = [loigiai_vdc_1]
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    random.shuffle(combined_vdc)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)
    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)
        if 1 <= true_count <= 3:
            break
    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]
    combined_nb = list(zip(list_nb_1, list_nb_2))
    combined_th = list(zip(list_th_1, list_th_2))
    combined_vd = list(zip(list_vd_1, list_vd_2))
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    random.shuffle(combined_nb)
    random.shuffle(combined_th)
    random.shuffle(combined_vd)
    random.shuffle(combined_vdc)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+
    str(noidungcauhoi)+ 
        '\n\\choiceTFn \n'
       '{'+str(shuffled_answers_nb[0])+'}\n'
       '{'+str(shuffled_answers_th[0])+'}\n'
       '{'+str(shuffled_answers_vd[0])+'}\n'
       '{'+str(shuffled_answers_vdc[0])+'}\n'
        '\\loigiai{ \n'
        '\\begin{enumEX}[a)]{1} \n'
        '\\item '+str(shuffled_solutions_nb[0])+'\n'
        '\\item '+str(shuffled_solutions_th[0])+'\n'
        '\\item '+str(shuffled_solutions_vd[0])+'\n'
        '\\item '+str(shuffled_solutions_vdc[0])+'\n'
        '\\end{enumEX}} \n'
        '\\end{ex}\n \\end{minipage} \n\n')
    return content
