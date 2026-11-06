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


def bt_dang4_p1_b4_c1_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                hinhve=('''\\begin{center} \n'''
                    '''\\scalebox{0.6}{\\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
                \\clip(-2.610726692660921,-1.084349895553466) rectangle (8.611077283703963,6.968944722778987);
                \\draw (0.,0.)-- (5.,0.);
                \\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (2.,2.);
                \\draw [dash pattern=on 2pt off 2pt] (2.,2.)-- (7.,2.);
                \\draw (7.,2.)-- (5.,0.);
                \\draw [dash pattern=on 2pt off 2pt] (3.,6.)-- (2.,2.);
                \\draw (3.,6.)-- (0.,0.);
                \\draw (3.,6.)-- (7.,2.);
                \\draw (3.,6.)-- (5.,0.);
                \\draw [dash pattern=on 2pt off 2pt] (0.,0.)-- (7.,2.);
                \\draw [dash pattern=on 2pt off 2pt] (2.,2.)-- (5.,0.);
                \\draw [dash pattern=on 2pt off 2pt] (2.5,4.)-- (1.5,3.);
                \\draw [dash pattern=on 2pt off 2pt] (1.5,3.)-- (4.5,2.);
                \\draw [dash pattern=on 2pt off 2pt] (4.5,2.)-- (2.5,4.);
                \\draw [dash pattern=on 2pt off 2pt] (4.5,2.)-- (3.5,1.);
                \\draw [dash pattern=on 2pt off 2pt] (1.5,3.)-- (3.5,1.);
                \\draw (2.6965264820434123,7.0-0.3) node[anchor=north west] {$S$};
                \\draw (-0.7,0.2) node[anchor=north west] {$D$};
                \\draw (5.099312745218011,0.2) node[anchor=north west] {$C$};
                \\draw (7.053226849338015,2.5) node[anchor=north west] {$B$};
                \\draw (2.6,4.55) node[anchor=north west] {$M$};
                \\draw (4.518419362912065,2.7) node[anchor=north west] {$P$};
                \\draw (3.1189943964477376,1) node[anchor=north west] {$O$};
                \\draw (0.8,3.5) node[anchor=north west] {$N$};
                \\draw (1.3499100048796262,2.4) node[anchor=north west] {$A$};
            \\end{tikzpicture}}\n'''
            '''\\end{center}\n''')
                #NHập đáp án đúng vào đây
                du = ['''$(MNP)//(SBC)$''',
                    '''$(OMN)//(SBC)$''',
                    '''$(OMP)//(SBC)$''',
                    '''$(ONP)//(SBC)$''',
                    '''$(MNOP)//(SBC)$''',
                    ]
                #Nhập lời giải ứng với đáp án đúng vào đây
                lg = [('''Ta có $MN$ là đường trung bình của tam giác $SAD$ suy ra $MN//AD$ $(1)$.\\\\ \n'''
                            '''\\hspace{1.5cm}$OP$ là đường trung bình của tam giác $BAD$ suy ra $OP//AD$ $(2)$.\\\\ \n'''
                            '''Từ $(1)$ và $(2)$ suy ra $MN//OP//AD\\Rightarrow M,N,O,P$ đồng phẳng.\\\\ \n'''
                            '''Lại có $MP//SB,OP//BC$ nên $(MNOP)//(SBC)$ hay $(MNP)//(SBC)$.'''
                            ),
                    ('''Ta có $MN$ là đường trung bình của tam giác $SAD$ suy ra $MN//AD$ $(1)$.\\\\ \n'''
                                '''\\hspace{1.5cm}$OP$ là đường trung bình của tam giác $BAD$ suy ra $OP//AD$.\\\\ \n'''
                                '''Từ $(1)$ và $(2)$ suy ra $MN//OP//AD\\Rightarrow M,N,O,P$ đồng phẳng.\\\\ \n'''
                                '''Lại có $MP//SB,OP//BC$ nên $(MNOP)//(SBC)$ hay $(OMN)//(SBC)$.'''
                                ),

                    ('''Ta có $MN$ là đường trung bình của tam giác $SAD$ suy ra $MN//AD$ $(1)$.\\\\ \n'''
                                '''\\hspace{1.5cm}$OP$ là đường trung bình của tam giác $BAD$ suy ra $OP//AD$.\\\\ \n'''
                                '''Từ $(1)$ và $(2)$ suy ra $MN//OP//AD\\Rightarrow M,N,O,P$ đồng phẳng.\\\\ \n'''
                                '''Lại có $MP//SB,OP//BC$ nên $(MNOP)//(SBC)$ hay $(OMP)//(SBC)$.'''
                                ),

                    ('''Ta có $MN$ là đường trung bình của tam giác $SAD$ suy ra $MN//AD$ $(1)$.\\\\ \n'''
                                '''\\hspace{1.5cm}$OP$ là đường trung bình của tam giác $BAD$ suy ra $OP//AD$.\\\\ \n'''
                                '''Từ $(1)$ và $(2)$ suy ra $MN//OP//AD\\Rightarrow M,N,O,P$ đồng phẳng.\\\\ \n'''
                                '''Lại có $MP//SB,OP//BC$ nên $(MNOP)//(SBC)$ hay $(ONP)//(SBC)$.'''
                                ),

                    ('''Ta có $MN$ là đường trung bình của tam giác $SAD$ suy ra $MN//AD$ $(1)$.\\\\ \n'''
                                '''\\hspace{1.5cm}$OP$ là đường trung bình của tam giác $BAD$ suy ra $OP//AD$.\\\\ \n'''
                                '''Từ $(1)$ và $(2)$ suy ra $MN//OP//AD\\Rightarrow M,N,O,P$ đồng phẳng.\\\\ \n'''
                                '''Lại có $MP//SB,OP//BC$ nên $(MNOP)//(SBC)$.'''
                                ),

                    ]

                combined = list(zip(du, lg))
                random.shuffle(combined)
                shuffled_answers, shuffled_solutions = zip(*combined)    
                da= shuffled_answers[0]

                #NHập đáp án sai vào đây
                s = ['''$(MNP)//(SCD)$''',
                    '''$(MNP)//(SAB)$''',
                    '''$(MNP)//(SAD)$''',
                    '''$(ONP)//(SCD)$''',
                    '''$(ONP)//(SAB)$''',
                    '''$(ONP)//(SAD)$''',
                            '''$(MN0)//(SCD)$''',
                        '''$(MN0)//(SAB)$''',
                        '''$(MN0)//(SAD)$''',
                        '''$(OMP)//(SCD)$''',
                        '''$(OMP)//(SAB)$''',
                        '''$(OMP)//(SAD)$''',
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Cho hình chóp $S.ABCD$. Đáy là hình bình hành tâm $O$. $M,N,P$ theo thứ tự là trung điểm của $SA,SD,AB$. Khẳng định nào sau đây đúng? \\\\ \n'''
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
                loigiai= shuffled_solutions[0]


            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(hinhve)+''+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

