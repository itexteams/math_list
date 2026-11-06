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


def bt_dang8_p1_b5_c2_hh11(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                a=randint(5,19)

                du = ['$%s$'%(latex(a*sqrt(5))),
                    ]
                da= random.choice(du)
                s = ['$%s$'%(latex((a+1)*sqrt(5))),
                    '$%s$'%(latex((a+2)*sqrt(5))),
                    '$%s$'%(latex((a+3)*sqrt(5))),
                    '$%s$'%(latex((a-1)*sqrt(5))),
                    '$%s$'%(latex((a-2)*sqrt(5))),
                    '$%s$'%(latex((a-3)*sqrt(5))),
                    ]

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)
                # Câu hỏi
                noidungcauhoi = ('''Một hình lập phương được tạo thành khi xếp miếng bìa carton như hình vẽ bên.
                            \\begin{center}
                \\definecolor{ududff}{rgb}{0.30196078431372547,0.30196078431372547,1.}
                \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
                    \\clip(-0.29664399652489554,-1.1234389471993134) rectangle (4.210808911551868,2.243189596532352);
                    \\draw [line width=1.pt] (0.,1.)-- (4.,1.);
                    \\draw [line width=1.pt] (4.,1.)-- (4.,0.);
                    \\draw [line width=1.pt] (4.,0.)-- (0.,0.);
                    \\draw [line width=1.pt] (0.,0.)-- (0.,1.);
                    \\draw [line width=1.pt] (1.,2.)-- (2.,2.);
                    \\draw [line width=1.pt] (2.,2.)-- (2.,-1.);
                    \\draw [line width=1.pt] (2.,-1.)-- (1.,-1.);
                    \\draw [line width=1.pt] (1.,-1.)-- (1.,2.);
                    \\draw [line width=1.pt] (3.,1.)-- (3.,0.);
                    \\draw (0.5,1.5) node[anchor=north west] {$A$};
                    \\draw (1.9,1.5) node[anchor=north west] {$B$};
                    \\draw (3.4,0.5439197391512035) node[anchor=north west] {$O$};
                    \\begin{scriptsize}
                        \\draw [fill=ududff] (3.4848297706049913,0.49605298260525565) circle (1.5pt);
                    \\end{scriptsize}
                \\end{tikzpicture}
            \\end{center}     
            Khoảng cách từ điểm $O$ đến đường thẳng $AB$ sau khi xếp bằng bao nhiêu? biết rằng độ dài đoạn thẳng $AB$ bằng $%s$.'''
                                %(latex(2*a)
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
                loigiai=('''\\begin{center}
                \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
                    \\clip(-0.7823559529893865,-0.43541016640061686) rectangle (6.990343708454726,4.799481818697665);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,0.)-- (2.,1.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,1.)-- (6.,1.);
                    \\draw [line width=1.pt] (6.,1.)-- (4.,0.);
                    \\draw [line width=1.pt] (4.,0.)-- (0.,0.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.,1.)-- (2.,4.);
                    \\draw [line width=1.pt] (2.,4.)-- (0.,3.);
                    \\draw [line width=1.pt] (0.,3.)-- (0.,0.);
                    \\draw [line width=1.pt] (2.,4.)-- (6.,4.);
                    \\draw [line width=1.pt] (6.,4.)-- (4.,3.);
                    \\draw [line width=1.pt] (4.,3.)-- (0.,3.);
                    \\draw [line width=1.pt] (4.,3.)-- (4.,0.);
                    \\draw [line width=1.pt] (6.,4.)-- (6.,1.);
                    \\draw [line width=1.pt] (0.9816097297005739,3.490804864850287)-- (2.9871910139677995,3.5040318751236486);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.9816097297005739,3.490804864850287)-- (1.0050863383235158,0.5025431691617579);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (2.9871910139677995,3.5040318751236486)-- (1.0050863383235158,0.5025431691617579);
                    \\draw (2.0527681038488352,1.5183831911208516) node[anchor=north west] {$A$};
                    \\draw (-0.3682367087321182,0.13798571026329237) node[anchor=north west] {$B$};
                    \\draw (4.049035230012077,0.08489349946107853) node[anchor=north west] {$C$};
                    \\draw (6.0346839140148765,1.1467377155053549) node[anchor=north west] {$D$};
                    \\draw (1.670504186072895,4.5764945333283675) node[anchor=north west] {$A'$};
                    \\draw (-0.4319473616947749,3.567742528086305) node[anchor=north west] {$B'$};
                    \\draw (4.070272114332963,3.1111495151872663) node[anchor=north west] {$C'$};
                    \\draw (6.045302356175319,4.555257649007482) node[anchor=north west] {$D'$};
                    \\draw (3.0402832247700133,3.8225851399369315) node[anchor=north west] {$O$};
                    \\draw (0.6086599700286174,4.013717098824901) node[anchor=north west] {$M$};
                    \\draw (1.054634540767214,0.605197165322774) node[anchor=north west] {$N$};
                \\end{tikzpicture}
            \\end{center}
                        Sau khi xếp miếng bìa lại ta được hình lập phương $ABCD.A'B'C'D'$ cạnh $%s$, $O$ là tâm của $A'B'C'D'$. \\\\
                        Gọi $M, N$ lần lượt là trung điểm các cạnh $AB, A'B$.\\\\
                        $\\Rightarrow MN = AA' = %s, OM = \\frac{1}{2}A'D' = %s$.\\\\
                        Lại có: $\\begin{cases} AB \\perp OM \\\\ AB \\perp MN \\end{cases} \\Rightarrow AB \\perp ON \\Rightarrow d(O,AB) = ON = \\sqrt{OM^2 + MN^2} =%s$.'''
                        %(latex(2*a),latex(2*a),latex(a),latex(a*sqrt(5))
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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

