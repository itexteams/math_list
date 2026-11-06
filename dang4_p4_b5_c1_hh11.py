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


def bt_dang4_p4_b5_c1_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                a=randint(2,9)

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho tứ diện $ABCD$. Gọi $M, N$ lần lượt là trung điểm của các cạnh $BC$ và $CD$. \\\\ \n'
                                'a) Tìm giao tuyến của hai mặt phẳng $(ADM)$ và $(ABN)$. \\\\ \n'
                                'b) Tìm hình chiếu của $M$ và $N$ qua phép chiếu song song lên mặt phẳng $(ABD)$ theo phương $CA$. \n'
                                %(
                                ))

                # Nội dung lời giải
                loigiai = (    ''' \\begin{center}
                        \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                    \\clip(-1.18,-2.84) rectangle (6.44,4.28);
                    \\draw [line width=1.pt] (0.,0.)-- (1.52,3.14);
                    \\draw [line width=1.pt] (1.52,3.14)-- (5.,0.);
                    \\draw [line width=1.pt] (0.,0.)-- (1.2,-2.);
                    \\draw [line width=1.pt] (1.2,-2.)-- (5.,0.);
                    \\draw [line width=1.pt] (1.52,3.14)-- (1.2,-2.);
                    \\draw [line width=1.pt,dash pattern=on 3pt off 3pt] (0.,0.)-- (5.,0.);
                    \\draw [line width=1.pt,dash pattern=on 3pt off 3pt] (0.,0.)-- (3.1,-1.);
                    \\draw [line width=1.pt,dash pattern=on 3pt off 3pt] (5.,0.)-- (0.6,-1.);
                    \\draw [line width=1.pt] (0.6,-1.)-- (0.76,1.57);
                    \\draw [line width=1.pt] (3.26,1.57)-- (3.1,-1.);
                    \\draw (1.14,3.8) node[anchor=north west] {$A$};
                    \\draw (-0.72,0.46) node[anchor=north west] {$B$};
                    \\draw (0.76,-1.86) node[anchor=north west] {$C$};
                    \\draw (5.06,0.4) node[anchor=north west] {$D$};
                    \\draw (-0.16,-0.7) node[anchor=north west] {$M$};
                    \\draw (3.04,-0.88) node[anchor=north west] {$N$};
                    \\draw (3.14,2.2) node[anchor=north west] {$P$};
                    \\draw (0.08,2.2) node[anchor=north west] {$Q$};
                    \\draw (1.74,-0.7) node[anchor=north west] {$O$};
                    \\draw [line width=1.pt,dash pattern=on 3pt off 3pt] (1.52,3.14)-- (2.0190943396226415,-0.6513207547169811);
                    \\end{tikzpicture}
                    \\end{center}
                        '''

                                '\\begin{enumEX}[a)]{1} \n'
                                '\\item  Ta thấy $A$ là một điểm chung của hai mặt phẳng. \\\\ \n'
                                'Gọi $O$ là giao điểm của $BN$ và $DM$, ta có \\\\ \n'
                                '\\hspace*{1cm} $O$ thuộc $BN$, $BN$ nằm trong mặt phẳng $(ABN)$ nên $O$ thuộc mặt phẳng $(ABN)$. \\\\ \n'
                                '\\hspace*{1cm} $O$ thuộc $DM$, $DM$ nằm trong mặt phẳng $(ADM)$ nên $O$ thuộc mặt phẳng $(ADM)$. \\\\ \n'
                                'Suy ra $O$ thuộc giao tuyến của hai mặt phẳng $(ABN)$ và $(ADM)$. \\\\ \n'
                                'Vậy $AO$ là giao tuyến của hai mặt phẳng $(ABN)$ và $(ADM)$. \n'
                                '\\item  Trong mặt phẳng $(ABC)$, dựng đường thẳng qua $M$ và song song với $AC$ và cắt $AB$ tại trung điểm $Q$ của $AB$. \\\\ \n'
                                'Vậy $Q$ là hình chiếu của $M$ lên mặt phẳng $(ABD)$ theo phương chiếu $CA$. \\\\ \n'
                                'Trong mặt phẳng $(ADC)$, dựng đường thẳng qua $N$ và song song với $AC$ và cắt $AD$ tại trung điểm $P$ của $AD$. \\\\ \n'
                                'Vậy $P$ là hình chiếu của $N$ lên mặt phẳng $(ABD)$ theo phương chiếu $CA$.'

                                '\\end{enumEX} \n'

                        %(
                        ))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content   

