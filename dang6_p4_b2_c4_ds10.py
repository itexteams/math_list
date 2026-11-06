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


def bt_dang6_p4_b2_c4_ds10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                x=symbols('x')
                k=randint(15,30)
                a=4*k
                x0=Rational(a,4)
                f=-2*x**2+a*x
                f0=-2*x0**2+a*x0

                # Nội dung câu hỏi
                noidungcauhoi = ('Một tấm tôn có bề rộng $AB$ là $%s$ cm. Người ta chọn $2$ điểm $M$ và $N$ trên đoạn $AB$ sao cho có thể làm được một máng nước như hình vẽ. \n'
                                '''
                                \\begin{center}
                                \\scalebox{0.6}{ 
                \\definecolor{zzttqq}{rgb}{0.6,0.2,0.}
                \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                    \\clip(-0.8604772150056869,-0.8086749947504395) rectangle (12.627153526151053,4.606340492448432);
                    \\fill[line width=1.pt ,color=zzttqq,fill=zzttqq,fill opacity=0.10000000149011612] (0.,0.) -- (4.,0.) -- (7.,3.) -- (3.,3.) -- cycle;
                    \\fill[line width=1.pt ,color=zzttqq,fill=zzttqq,fill opacity=0.10000000149011612] (7.,0.) -- (9.,0.) -- (12.137246936311493,3.174677918941899) -- (10.137246936311493,3.174677918941899) -- cycle;
                    \\fill[line width=1.pt ,color=zzttqq,fill=zzttqq,fill opacity=0.10000000149011612] (10.137246936311493,3.174677918941899) -- (10.,4.) -- (7.,1.) -- (7.,0.) -- cycle;
                    \\fill[line width=1.pt ,color=zzttqq,fill=zzttqq,fill opacity=0.10000000149011612] (12.137246936311493,3.174677918941899) -- (12.,4.) -- (9.,1.) -- (9.,0.) -- cycle;
                    \\draw [line width=1.pt ,color=zzttqq] (0.,0.)-- (4.,0.);
                    \\draw [line width=1.pt ,color=zzttqq] (4.,0.)-- (7.,3.);
                    \\draw [line width=1.pt ,color=zzttqq] (7.,3.)-- (3.,3.);
                    \\draw [line width=1.pt ,color=zzttqq] (3.,3.)-- (0.,0.);
                    \\draw [line width=1.pt ,color=zzttqq] (7.,0.)-- (9.,0.);
                    \\draw [line width=1.pt ,color=zzttqq] (9.,0.)-- (12.137246936311493,3.174677918941899);
                    \\draw [line width=1.pt ,color=zzttqq] (12.137246936311493,3.174677918941899)-- (10.137246936311493,3.174677918941899);
                    \\draw [line width=1.pt ,color=zzttqq] (10.137246936311493,3.174677918941899)-- (7.,0.);
                    \\draw [line width=1.pt ,color=zzttqq] (10.137246936311493,3.174677918941899)-- (10.,4.);
                    \\draw [line width=1.pt ,color=zzttqq] (10.,4.)-- (7.,1.);
                    \\draw [line width=1.pt ,color=zzttqq] (7.,1.)-- (7.,0.);
                    \\draw [line width=1.pt ,color=zzttqq] (7.,0.)-- (10.137246936311493,3.174677918941899);
                    \\draw [line width=1.pt ,color=zzttqq] (12.137246936311493,3.174677918941899)-- (12.,4.);
                    \\draw [line width=1.pt ,color=zzttqq] (12.,4.)-- (9.,1.);
                    \\draw [line width=1.pt ,color=zzttqq] (9.,1.)-- (9.,0.);
                    \\draw [line width=1.pt ,color=zzttqq] (9.,0.)-- (12.137246936311493,3.174677918941899);
                    \\draw [line width=1.pt ] (3.,3.)-- (0.,0.);
                    \\draw [line width=1.pt ] (0.,0.)-- (4.,0.);
                    \\draw [line width=1.pt ] (4.,0.)-- (7.,3.);
                    \\draw [line width=1.pt ] (7.,3.)-- (3.,3.);
                    \\draw [line width=1.pt ,dash pattern=on 2pt off 2pt] (1.,0.)-- (4.,3.);
                    \\draw [line width=1.pt ,dash pattern=on 2pt off 2pt] (3.,0.)-- (6.,3.);
                    \\draw [line width=1.pt ] (10.,4.)-- (7.,1.);
                    \\draw [line width=1.pt ] (7.,1.)-- (7.,0.);
                    \\draw [line width=1.pt ] (7.,0.)-- (10.137246936311493,3.174677918941899);
                    \\draw [line width=1.pt ] (10.137246936311493,3.174677918941899)-- (10.,4.);
                    \\draw [line width=1.pt ] (12.,4.)-- (9.,1.);
                    \\draw [line width=1.pt ] (9.,1.)-- (9.,0.);
                    \\draw [line width=1.pt ] (9.,0.)-- (7.,0.);
                    \\draw [line width=1.pt ] (9.,0.)-- (12.137246936311493,3.174677918941899);
                    \\draw [line width=1.pt ] (12.137246936311493,3.174677918941899)-- (12.,4.);
                    \\draw [line width=1.pt ] (10.137246936311493,3.174677918941899)-- (11.137246936311493,3.174677918941899);
                    \\draw [line width=1.pt ,dash pattern=on 2pt off 2pt] (11.137246936311493,3.174677918941899)-- (12.137246936311493,3.174677918941899);
                    \\draw (-0.61,0.2643465073212263) node[anchor=north west] {$A$};
                    \\draw (4.080412492208068,0.16453055364014108) node[anchor=north west] {$B$};
                    \\draw (0.6118081017903308,0) node[anchor=north west] {$M$};
                    \\draw (2.6580351522525927,0) node[anchor=north west] {$N$};
                    \\draw (6.4,1.4496609572841128) node[anchor=north west] {$A$};
                    \\draw (8.5,1.4746149457043842) node[anchor=north west] {$B$};
                    \\draw (6.53838035160481,0) node[anchor=north west] {$M$};
                    \\draw (8.871578268900194,0) node[anchor=north west] {$N$};
                \\end{tikzpicture} }
            \\end{center}
                                '''
                                'Biết $AMNB$ là hình chữ nhật. Tìm $MN$ để máng nước có diện tích bề mặt ngang $AMNB$ lớn nhất. \n'
                                %(latex(a)
                                ))

                # Nội dung lời giải
                loigiai = ('Đặt $MN=2x$ với $0<x<%s$ suy ra $AM=NB=%s-x$. \\\\ \n'
                        'Diện tích bề mặt ngang là $S=2x(%s-x)=-2x^2+%s x$.\\\\ \n'
                        'Parabol có đỉnh là $\\left(%s; %s \\right)$.\\\\ \n'
                        'Vậy diện tích bề mặt ngang lớn nhất bằng $%s$ cm$^2$ khi $MN=%s$ cm.'
                        %(latex(Rational(a,2)),latex(Rational(a,2)),
                            latex(Rational(a,2)),latex(a),
                            latex(x0),latex(f0),
                            latex(f0),latex(2*x0)
                        ))


            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')   
            return content

